from sklearn.linear_model import Lasso
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
import numpy as np
import pandas as pd
from symbal.utils import get_equation


class LassoEnsemble:

    def __init__(self, alpha_range=(1e-4, 1e3), num_models=20, scaler=MinMaxScaler(),
                 polynomial=PolynomialFeatures(degree=2), max_iter=50000, progress=True, equation_file=None):

        self.best_model = None
        alpha_list = np.geomspace(alpha_range[0], alpha_range[1], num_models)
        self.models = [Lasso(alpha=alpha, max_iter=max_iter) for alpha in alpha_list]
        self.scaler = scaler
        self.polynomial = polynomial
        self.column_list = None
        self.equations_ = None
        self.eq_ = None
        self.equation_file = equation_file
        self.progress = progress

    def fit(self, x: pd.DataFrame, y: pd.Series):

        self.column_list = list(x.columns)
        x = np.array(x)
        y = np.array(y)

        x_poly = self.polynomial.fit_transform(x)
        if self.scaler is not None:
            x_poly_scale = self.scaler.fit_transform(x_poly)
        else:
            x_poly_scale = x_poly

        complexities, losses, equations = [[], [], []]

        for model in self.models:

            model.fit(x_poly_scale, y)
            complexities.append(np.sum(model.coef_.astype(bool)))
            losses.append(np.sqrt(np.mean((y - model.predict(x_poly_scale)) ** 2)))
            equations.append(get_equation(self.column_list, model, self.scaler, self.polynomial))

        self.eq_ = pd.DataFrame(np.array([losses, complexities, equations]).T,
                                columns=['loss', 'complexity', 'equation'])
        idmax = list(self.eq_.groupby('complexity')['loss'].idxmax())
        self.eq_ = self.eq_.iloc[idmax, :].reset_index(drop=True)
        self.models = [model for i, model in enumerate(self.models) if i in idmax]

        self.eq_['AIC'] = len(x) * np.log(self.eq_['loss'] / len(x)) + 2 * self.eq_['complexity']
        self.eq_.loc[0, 'AIC'] = 0
        self.eq_.loc[0, 'pareto'] = 0

        for i, _ in range(self.eq_.shape[0]):
            if i > 0:

                idmin = self.eq_.loc[:i-1, :]['loss'].idxmin()
                self.eq_.loc[i, 'pareto'] = ((self.eq_.loc[i, 'AIC'] - self.eq_.loc[idmin, 'AIC']) / (
                        self.eq_.loc[i, 'complexity'] - self.eq_.loc[idmin, 'complexity']))

        self.eq_.loc[0:1, 'pareto'] = 0

        self.eq_['nPar'] = (self.eq_['pareto'] - np.mean(self.eq_['pareto'])) / np.std(self.eq_['pareto'])
        self.eq_['score'] = np.exp((np.min(self.eq_['nPar']) - self.eq_['nPar']) / 2)

        self.eq_ = self.eq_[self.eq_['pareto'] <= 0]
        self.models = [model for i, model in enumerate(self.models) if i in list(self.eq_.index)]
        self.eq_ = self.eq_.reset_index(drop=True)

        best_index = self.eq_['pareto'].idxmin()
        self.best_model = self.eq_.loc[best_index, 'model']
        self.eq_['model'] = self.models

        self.equations_ = self.eq_

        if self.progress:
            self.equations_.to_csv(f'{self.equation_file}.csv')

    def predict(self, x: pd.DataFrame, num=None):

        x = x[self.column_list]
        x = np.array(x)

        x_poly = self.polynomial.transform(x)
        if self.scaler is not None:
            x_poly_scale = self.scaler.transform(x_poly)
        else:
            x_poly_scale = x_poly

        if num is None:
            y_pred = self.best_model.predict(x_poly_scale)
        else:
            y_pred = self.equations_.loc[num, 'model'].predict(x_poly_scale)
        return y_pred
