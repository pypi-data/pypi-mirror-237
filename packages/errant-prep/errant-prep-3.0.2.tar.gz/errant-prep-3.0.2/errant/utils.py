from __future__ import annotations

import spacy

from errant.constants import MAPPING_ERRANT_ACA


def get_available_spacy_models() -> list[str]:
    """
    Get a list of available spaCy models installed in the current environment.

    Returns:
        List[Text]: A list of available spaCy model names.
    """
    installed_models = spacy.info().get('pipelines', '')
    if not installed_models:
        return []
    return list(installed_models.keys())


def get_spacy_models_for_language(lang: str) -> list[str]:
    """
    Get a list of spaCy models that support a specific language.

    Args:
        lang (Text): The language code (e.g., 'en' for English) to filter models by.

    Returns:
        List[Text]: A list of spaCy model names that support the specified language.
    """
    installed_models = get_available_spacy_models()
    if not installed_models:
        return []

    return [
        model_name
        for model_name in installed_models
        if model_name.split('_')[0] == lang
    ]


def convert_errant_to_prep_result(best_dict, best_cats):
    result = {}
    for error_cat, value in best_cats.items():
        tp, fp, fn = value[0], value[1], value[2]

        type_error = error_cat[2:]
        opra_error = error_cat[:2]

        type_error = MAPPING_ERRANT_ACA[type_error]
        error_cat = opra_error + type_error
        if error_cat not in result:
            result[error_cat] = [0, 0, 0]
        result[error_cat][0] += tp
        result[error_cat][1] += fp
        result[error_cat][2] += fn

    return best_dict, result
