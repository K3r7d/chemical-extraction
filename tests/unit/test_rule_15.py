"""Rule 15 consistency-gate unit tests."""

from __future__ import annotations

import pytest

from a2i2_extraction.validators import check_rule_15

pytestmark = pytest.mark.unit


def test_clean_sample_has_no_rule15_errors(sample_extraction):
    errors = [i for i in check_rule_15(sample_extraction) if i.severity.value == "error"]
    assert errors == []


def test_a_dangling_reference(sample_extraction):
    sample_extraction["synthesis"][0]["steps"][0]["reactants"][0][
        "compound_id"
    ] = "C99"
    codes = {i.code for i in check_rule_15(sample_extraction)}
    assert "rule15_a_dangling_reference" in codes


def test_b_target_missing(sample_extraction):
    sample_extraction["synthesis"][0]["target_compound_id"] = "C99"
    codes = {i.code for i in check_rule_15(sample_extraction)}
    assert "rule15_b_target_missing" in codes


def test_c_duplicate_id(sample_extraction):
    sample_extraction["compounds"].append(dict(sample_extraction["compounds"][0]))
    codes = {i.code for i in check_rule_15(sample_extraction)}
    assert "rule15_c_duplicate_id" in codes


def test_c_noncontiguous_ids(sample_extraction):
    sample_extraction["compounds"][2]["id"] = "C05"
    # need to fix references too so the dangling-ref check doesn't dominate
    sample_extraction["synthesis"][0]["target_compound_id"] = "C05"
    sample_extraction["synthesis"][0]["steps"][0]["product"]["compound_id"] = "C05"
    codes = {i.code for i in check_rule_15(sample_extraction)}
    assert "rule15_c_noncontiguous_ids" in codes


def test_d_reactant_is_product(sample_extraction):
    sample_extraction["synthesis"][0]["steps"][0]["reactants"][0][
        "compound_id"
    ] = "C03"
    codes = {i.code for i in check_rule_15(sample_extraction)}
    assert "rule15_d_reactant_is_product" in codes


def test_f_final_product_purity_missing_method(sample_extraction):
    sample_extraction["compounds"][2]["purity"] = "99.0%"  # no method
    codes = {i.code for i in check_rule_15(sample_extraction)}
    assert "rule15_f_purity_missing_method" in codes


def test_g_multiple_iterative_couplings(sample_extraction):
    pathway = sample_extraction["synthesis"][0]
    pathway["steps"][0]["reaction_type"] = "iterative SPPS assembly"
    extra_step = dict(pathway["steps"][0])
    extra_step["step_number"] = 2
    pathway["steps"].append(extra_step)
    codes = {i.code for i in check_rule_15(sample_extraction)}
    assert "rule15_g_multiple_iterative_couplings" in codes
