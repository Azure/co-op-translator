from co_op_translator.utils.markdown.anchors import normalize_internal_anchor_links


def test_normalize_internal_anchor_links_does_not_change_translated_headings():
    source = """## Section One

- [Go](#section-one)
"""
    translated = """## 섹션 하나

- [이동](#section-one)
"""

    result = normalize_internal_anchor_links(source, translated)

    assert "## 섹션 하나" in result
    assert "## Section One" not in result


def test_normalize_internal_anchor_links_handles_missing_links_without_positional_mapping():
    source = """## A
## B

- [A](#a)
- [B](#b)
"""
    translated = """## 에이
## 비

- [에이](#a)
"""

    result = normalize_internal_anchor_links(source, translated)

    assert "(#에이)" in result
    assert "- [에이](#a)" not in result


def test_normalize_internal_anchor_links_handles_reordered_toc_links():
    source = """## A
## B

- [A](#a)
- [B](#b)
"""
    translated = """## 에이
## 비

- [비](#b)
- [에이](#a)
"""

    result = normalize_internal_anchor_links(source, translated)

    # Reordered links should still map to their own translated headings.
    assert "- [비](#비)" in result
    assert "- [에이](#에이)" in result


def test_normalize_internal_anchor_links_ignores_headings_inside_fenced_code():
    source = """## Real Section

~~~md
## Fake Section
~~~

- [Go](#real-section)
"""
    translated = """## 실제 섹션

~~~md
## 가짜 섹션
~~~

- [이동](#real-section)
"""

    result = normalize_internal_anchor_links(source, translated)

    assert "- [이동](#실제-섹션)" in result


def test_normalize_internal_anchor_links_matches_translated_headings():
    source = """# Fine-tune and Integrate custom Phi-3 models with Prompt flow

## Table of Contents

1. [Scenario 1](#scenario-1-set-up-azure-resources-and-prepare-for-fine-tuning)
1. [Scenario 2](#scenario-2-fine-tune-phi-3-model-and-deploy-in-azure-machine-learning-studio)

## Scenario 1: Set up Azure resources and Prepare for fine-tuning
text

## Scenario 2: Fine-tune Phi-3 model and Deploy in Azure Machine Learning Studio
text
"""

    translated = """# Phi-3 모델 파인튜닝 및 Prompt flow 통합

## 목차

1. [시나리오 1](#scenario-1-set-up-azure-resources-and-prepare-for-fine-tuning)
1. [시나리오 2](#scenario-2-fine-tune-phi-3-model-and-deploy-in-azure-machine-learning-studio)

## 시나리오 1: 파인튜닝 준비 및 Azure 리소스 구성
내용

## 시나리오 2: Phi-3 파인튜닝 및 Azure Machine Learning Studio 배포
내용
"""

    result = normalize_internal_anchor_links(source, translated)

    assert "(#시나리오-1-파인튜닝-준비-및-azure-리소스-구성)" in result
    assert (
        "(#시나리오-2-phi-3-파인튜닝-및-azure-machine-learning-studio-배포)" in result
    )
