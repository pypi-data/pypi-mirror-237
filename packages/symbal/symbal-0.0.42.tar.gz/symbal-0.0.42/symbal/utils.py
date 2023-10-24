import copy

import numpy as np
from symbal.penalties import invquad_penalty
import pandas as pd
import warnings
import itertools
import sympy

from sklearn.preprocessing import MinMaxScaler, StandardScaler, PolynomialFeatures
from sklearn.linear_model import Lasso
from typing import Union, List


def new_penalty(penalty_array, penalty_function, a, b, by_range, batch_size):
    """
    Selects maximum from given values and penalizes area around selection.

    Assumes first column in penalty_array is penalized value, other columns are
    independent variables.

    Returns: independent variables for selected point & new penalty_array w/ penalized values
    """

    max_index = np.nanargmax(penalty_array[:, 0])  # index for largest value
    penalty_array[max_index, 0] = np.nan
    max_pos = penalty_array[max_index, 1:]  # independent variable values for this index

    r_x = np.abs(penalty_array[:, 1:] - max_pos)  # Distance to selected point for each variable
    if by_range:
        s_x = np.ptp(penalty_array[:, 1:], axis=0) / batch_size  # Tune width of penalty by range / batch_size
    else:
        s_x = np.nanstd(penalty_array[:, 1:],
                        axis=0)  # Tune width of penalty by standard deviation of each independent variable
    s_y = np.nanstd(penalty_array[:, 0], axis=0)  # Standard deviation of penalized value

    penalty = penalty_function(a, b, r_x, s_x, s_y)
    penalty_array[:, 0] -= penalty  # subtract penalty

    return max_index, penalty_array


def batch_selection(uncertainty_array, penalty_function=invquad_penalty, a=1, b=1, by_range=False, batch_size=10,
                    **kwargs):

    captured_penalties = pd.DataFrame()
    selected_indices = []
    penalty_array = uncertainty_array

    for i in range(batch_size):

        selected_index, penalty_array = new_penalty(penalty_array, penalty_function, a, b, by_range, batch_size)

        captured_penalties[f'{i}'] = penalty_array[:, 0]
        selected_indices.append(selected_index)

    return selected_indices, captured_penalties


def get_score(input_df, pysr_model):  # TODO - NaN filtering?

    predicted = pysr_model.predict(input_df)
    actual = np.array(input_df['output'])
    score = np.nanmean(np.abs(predicted - actual))

    return score


def get_metrics(pysr_model):

    best_index = np.argmax(pysr_model.equations_['score'])
    equation = pysr_model.equations_.loc[best_index, 'equation']
    loss = pysr_model.equations_.loc[best_index, 'loss']
    score = pysr_model.equations_.loc[best_index, 'score']

    other_equations = pysr_model.equations_.drop(best_index, axis=0)
    loss_other = np.mean(other_equations['loss'])
    score_other = np.mean(other_equations['score'])

    return equation, loss, score, loss_other, score_other


def get_gradient(cand_df, pysr_model, num=None, difference=None):

    if difference is None:
        difference = 1e-8

    overall = copy.deepcopy(cand_df)
    diff_dict = {
        column: pd.concat([cand_df.loc[:, column] + difference, cand_df.drop(column, axis=1)], axis=1)
        for column in cand_df
    }
    for column in cand_df:
        if num is not None:
            overall.loc[:, f'fh__{column}'] = pysr_model.predict(diff_dict[column], num)
            overall.loc[:, f'd__{column}'] = (overall.loc[:, f'fh__{column}'] -
                                              pysr_model.predict(cand_df, num)) / difference
        else:
            overall.loc[:, f'fh__{column}'] = pysr_model.predict(diff_dict[column])
            overall.loc[:, f'd__{column}'] = (overall.loc[:, f'fh__{column}'] -
                                              pysr_model.predict(cand_df)) / difference

    grad_string = 'sqrt('
    for column in overall:
        if 'd__' in column:
            grad_string += f'{column}**2 + '
    grad_string = grad_string.rstrip(' + ') + ')'
    overall['grad'] = overall.eval(grad_string)

    return np.array(overall['grad'])


def get_curvature(cand_df, pysr_model, num=None, difference=None):

    if difference is None:
        difference = 1e-8

    overall = copy.deepcopy(cand_df)
    diff_dict = {
        column: pd.concat([cand_df.loc[:, column] + difference, cand_df.drop(column, axis=1)], axis=1)
        for column in cand_df
    }
    diff2_dict = {
        column: pd.concat([cand_df.loc[:, column] + 2*difference, cand_df.drop(column, axis=1)], axis=1)
        for column in cand_df
    }
    for column in cand_df:
        if num is not None:
            overall.loc[:, f'fh__{column}'] = pysr_model.predict(diff_dict[column], num)
            overall.loc[:, f'f2h__{column}'] = pysr_model.predict(diff2_dict[column], num)
            overall.loc[:, f'd2__{column}'] = (pysr_model.predict(cand_df, num) - 2*overall.loc[:, f'fh__{column}'] +
                                               overall.loc[:, f'f2h__{column}']) / difference ** 2
        else:
            overall.loc[:, f'fh__{column}'] = pysr_model.predict(diff_dict[column])
            overall.loc[:, f'f2h__{column}'] = pysr_model.predict(diff2_dict[column])
            overall.loc[:, f'd2__{column}'] = (pysr_model.predict(cand_df) - 2*overall.loc[:, f'fh__{column}'] +
                                               overall.loc[:, f'f2h__{column}']) / difference ** 2

    lapl_string = ''
    for column in overall:
        if 'd2__' in column:
            lapl_string += f'abs({column}) + '
    lapl_string = lapl_string.rstrip(' + ')
    overall['lapl'] = overall.eval(lapl_string)

    return np.array(overall['lapl'])


def get_all_gradients(cand_df, pysr_model, difference=1e-8):

    gradients = np.empty((len(cand_df), len(pysr_model.equations_['equation'])))

    for j, _ in enumerate(pysr_model.equations_['equation']):
        gradients[:, j] = get_gradient(cand_df, pysr_model, num=j, difference=difference)

    return gradients


def get_uncertainties(cand_df, pysr_model):

    uncertainties = np.empty((len(cand_df), len(pysr_model.equations_['equation'])))
    equation_best = pysr_model.predict(cand_df)

    for j, _ in enumerate(pysr_model.equations_['equation']):
        uncertainties[:, j] = pysr_model.predict(cand_df, j) - equation_best

    return uncertainties


class CustomStrPrinter(sympy.printing.str.StrPrinter):
    def _print_Float(self, expr):
        return f'{expr:.3e}'


def get_equation(column_list: List[str], model: Lasso, scaler: Union[MinMaxScaler, StandardScaler],
                 polynomial: PolynomialFeatures):

    if isinstance(scaler, StandardScaler):
        warnings.warn('Equation identification not yet implemented for StandardScaler.')
        return ''

    if polynomial.interaction_only:
        warnings.warn('Equation identification not yet implemented for interaction_only option.')
        return ''

    variable_list = ['1', *column_list]
    variable_list.extend(list(itertools.combinations_with_replacement(column_list, polynomial.degree)))
    variable_list = np.array(['*'.join(var) if isinstance(var, tuple) else var for var in variable_list])

    lasso_coef = model.coef_
    scaler_range = scaler.data_range_
    scaler_min = scaler.data_min_
    intercept = model.intercept_

    variable_list = variable_list[lasso_coef > 0]
    scaler_range = scaler_range[lasso_coef > 0]
    scaler_min = scaler_min[lasso_coef > 0]
    lasso_coef = lasso_coef[lasso_coef > 0]

    unscaled_coef = lasso_coef * scaler_range
    adj_intercept = intercept + np.sum(lasso_coef * scaler_min)

    equation_terms = [f'{coef:.3e}*{feat}' for coef, feat in zip(unscaled_coef, variable_list)]
    equation = ' + '.join(equation_terms)
    equation += f' + {adj_intercept:.3e}'

    parsed_equation = CustomStrPrinter().doprint(sympy.parsing.sympy_parser.parse_expr(equation))

    return parsed_equation

