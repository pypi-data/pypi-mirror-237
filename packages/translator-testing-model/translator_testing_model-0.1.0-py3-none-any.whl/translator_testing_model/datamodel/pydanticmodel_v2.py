from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, Field
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "0.0.0"

class ConfiguredBaseModel(BaseModel,
                validate_assignment = True,
                validate_default = True,
                extra = 'forbid',
                arbitrary_types_allowed = True,
                use_enum_values = True):
    pass


class TestSourceEnum(str, Enum):
    
    # (External) Subject Matter Expert
    SME = "SME"
    # Subject Matter User Reasonably Familiar, generally Translator-internal biomedical science expert
    SMURF = "SMURF"
    # Git hub hosted issue from which a test asset/case/suite may be derived.
    GitHubUserFeedback = "GitHubUserFeedback"
    # Technical Advisory Committee, generally posting semantic use cases as Translator Feedback issues
    TACT = "TACT"
    # Curated benchmark tests
    BenchMark = "BenchMark"
    # Translator funded KP or ARA team generating test assets/cases/suites for their resources.
    TranslatorTeam = "TranslatorTeam"
    # Current SRI_Testing-like test data edges specific to KP or ARA components
    TestDataLocation = "TestDataLocation"
    
    

class TestObjectiveEnum(str, Enum):
    
    # Acceptance (pass/fail) test
    AcceptanceTest = "AcceptanceTest"
    # Semantic benchmarking
    BenchmarkTest = "BenchmarkTest"
    # Quantitative test
    QuantitativeTest = "QuantitativeTest"
    
    

class TestPersonaEnum(str, Enum):
    
    
    All = "All"
    # An MD or someone working in the clinical field.
    Clinical = "Clinical"
    # Looking for an answer for a specific patient.
    LookUp = "LookUp"
    # Someone working on basic biology questions or drug discoveries where the study of the biological mechanism.
    Mechanistic = "Mechanistic"
    
    

class ExpectedOutputEnum(str, Enum):
    """
    Expected output values for instances of Test Asset or Test Cases(?). (Note: does this Enum overlap with 'ExpectedResultsEnum' below?)
    """
    
    Acceptable = "Acceptable"
    
    BadButForgivable = "BadButForgivable"
    
    NeverShow = "NeverShow"
    
    number_1_TopAnswer = "1_TopAnswer"
    
    number_4_NeverShow = "4_NeverShow"
    
    

class ExpectedResultsEnum(str, Enum):
    """
    Does this Enum overlap with 'ExpectedOutputEnum' above?
    """
    # The query should return the result in this test case
    include_good = "include_good"
    # The query should not return the result in this test case
    exclude_bad = "exclude_bad"
    
    

class TestIssueEnum(str, Enum):
    
    
    causes_not_treats = "causes not treats"
    # Text Mining Knowledge Provider generated relationship?
    TMKP = "TMKP"
    
    category_too_generic = "category too generic"
    
    contraindications = "contraindications"
    
    chemical_roles = "chemical roles"
    
    

class SemanticSeverityEnum(str, Enum):
    """
    From Jenn's worksheet, empty or ill defined (needs elaboration)
    """
    
    High = "High"
    
    Low = "Low"
    
    NotApplicable = "NotApplicable"
    
    

class DirectionEnum(str, Enum):
    
    
    increased = "increased"
    
    decreased = "decreased"
    
    

class EnvironmentEnum(str, Enum):
    
    
    DEV = "DEV"
    
    CI = "CI"
    
    TEST = "TEST"
    
    PROD = "PROD"
    
    

class TestEntity(ConfiguredBaseModel):
    """
    Abstract global 'identification' class shared as a parent with all major model classes within the data model for Translator testing.
    """
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    

class TestMetadata(TestEntity):
    """
    Represents metadata related to (external SME, SMURF, Translator feedback,  large scale batch, etc.) like the provenance of test assets, cases and/or suites.
    """
    test_source: Optional[TestSourceEnum] = Field(None, description="""Provenance of a specific set of test assets, cases and/or suites.""")
    test_reference: Optional[str] = Field(None, description="""Source documentation where original test particulars are registered (e.g. Github repo)""")
    test_objective: Optional[TestObjectiveEnum] = Field(None, description="""Testing objective behind specified set of test particulars (e.g. acceptance pass/fail; benchmark; quantitative)""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    

class TestAsset(TestEntity):
    """
    Represents a Test Asset, which is a single specific instance of TestCase-agnostic semantic parameters representing the specification of a Translator test target with inputs and (expected) outputs.
    """
    input_id: Optional[str] = Field(None)
    input_name: Optional[str] = Field(None)
    output_id: Optional[str] = Field(None)
    output_name: Optional[str] = Field(None)
    expected_output: Optional[ExpectedOutputEnum] = Field(None)
    test_issue: Optional[TestIssueEnum] = Field(None)
    semantic_severity: Optional[SemanticSeverityEnum] = Field(None)
    in_v1: Optional[bool] = Field(None)
    well_known: Optional[bool] = Field(None)
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""One or more 'tags' slot values (inherited from TestEntity) should generally be defined to specify TestAsset membership in a \"Block List\" collection  """)
    

class TestAssetCollection(TestEntity):
    """
    Represents an ad hoc list of Test Assets.
    """
    test_assets: Dict[str, TestCase] = Field(default_factory=dict, description="""List of explicitly enumerated Test Assets.""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""One or more 'tags' slot values (inherited from TestEntity) should generally be defined as filters to specify TestAsset membership in a \"Block List\" collection  """)
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    

class QueryAnswerPair(TestAsset):
    """
    Represents a QueryAnswerPair specification of a Test Asset
    """
    input_id: Optional[str] = Field(None)
    input_name: Optional[str] = Field(None)
    output_id: Optional[str] = Field(None)
    output_name: Optional[str] = Field(None)
    expected_output: Optional[ExpectedOutputEnum] = Field(None)
    test_issue: Optional[TestIssueEnum] = Field(None)
    semantic_severity: Optional[SemanticSeverityEnum] = Field(None)
    in_v1: Optional[bool] = Field(None)
    well_known: Optional[bool] = Field(None)
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""One or more 'tags' slot values (inherited from TestEntity) should generally be defined to specify TestAsset membership in a \"Block List\" collection  """)
    

class TestEdgeData(TestAsset):
    """
    Represents a single Biolink Model compliant instance of an edge that can be used for testing.
    """
    input_id: Optional[str] = Field(None)
    input_name: Optional[str] = Field(None)
    output_id: Optional[str] = Field(None)
    output_name: Optional[str] = Field(None)
    expected_output: Optional[ExpectedOutputEnum] = Field(None)
    test_issue: Optional[TestIssueEnum] = Field(None)
    semantic_severity: Optional[SemanticSeverityEnum] = Field(None)
    in_v1: Optional[bool] = Field(None)
    well_known: Optional[bool] = Field(None)
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""One or more 'tags' slot values (inherited from TestEntity) should generally be defined to specify TestAsset membership in a \"Block List\" collection  """)
    

class TestCase(TestEntity):
    """
    Represents a single enumerated instance of Test Case, derived from a  given TestAsset and used to probe a particular test condition.
    """
    inputs: Optional[List[str]] = Field(default_factory=list)
    outputs: Optional[List[str]] = Field(default_factory=list)
    preconditions: Optional[List[str]] = Field(default_factory=list)
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    

class TestCaseSpecification(TestEntity):
    """
    Parameterized declaration of the Test Case generator which dynamically generates a collection of Test Cases from Test Assets, using applicable heuristics.
    """
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    

class TestSuite(TestEntity):
    """
    Specification of a set of Test Cases, one of either with a static list of 'test_cases' or a dynamic 'test_case_specification' slot values. Note: at least one slot or the other, but generally not both(?) needs to be present.
    """
    test_metadata: Optional[str] = Field(None, description="""Test metadata describes the external provenance, cross-references and objectives for a given test.""")
    test_persona: Optional[TestPersonaEnum] = Field(None, description="""A Test persona describes the user or operational context of a given test.""")
    test_cases: Optional[Dict[str, TestCase]] = Field(default_factory=dict, description="""List of explicitly enumerated Test Cases.""")
    test_case_specification: Optional[str] = Field(None, description="""Declarative specification of a set of Test Cases generated elsewhere (i.e. within a Test Runner)""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    

class AcceptanceTestCase(TestCase):
    """
    Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.
    """
    inputs: List[str] = Field(default_factory=list)
    outputs: List[str] = Field(default_factory=list)
    preconditions: Optional[List[str]] = Field(default_factory=list)
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    

class AcceptanceTestSuite(TestSuite):
    
    test_metadata: Optional[str] = Field(None, description="""Test metadata describes the external provenance, cross-references and objectives for a given test.""")
    test_persona: Optional[TestPersonaEnum] = Field(None, description="""A Test persona describes the user or operational context of a given test.""")
    test_cases: Optional[Dict[str, TestCase]] = Field(default_factory=dict, description="""List of explicitly enumerated Test Cases.""")
    test_case_specification: Optional[str] = Field(None, description="""Declarative specification of a set of Test Cases generated elsewhere (i.e. within a Test Runner)""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    

class BenchmarkTestSuite(ConfiguredBaseModel):
    """
    JsonObj(is_a='TestSuite')
    """
    None
    

class StandardsComplianceTestSuite(TestSuite):
    """
    Test suite for testing Translator components against releases of standards like TRAPI and the Biolink Model.
    """
    test_metadata: Optional[str] = Field(None, description="""Test metadata describes the external provenance, cross-references and objectives for a given test.""")
    test_persona: Optional[TestPersonaEnum] = Field(None, description="""A Test persona describes the user or operational context of a given test.""")
    test_cases: Optional[Dict[str, TestCase]] = Field(default_factory=dict, description="""List of explicitly enumerated Test Cases.""")
    test_case_specification: Optional[str] = Field(None, description="""Declarative specification of a set of Test Cases generated elsewhere (i.e. within a Test Runner)""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    

class OneHopTestSuite(TestSuite):
    """
    Test case for testing the integrity of \"One Hop\" knowledge graph retrievals sensa legacy SRI_Testing harness.
    """
    test_metadata: Optional[str] = Field(None, description="""Test metadata describes the external provenance, cross-references and objectives for a given test.""")
    test_persona: Optional[TestPersonaEnum] = Field(None, description="""A Test persona describes the user or operational context of a given test.""")
    test_cases: Optional[Dict[str, TestCase]] = Field(default_factory=dict, description="""List of explicitly enumerated Test Cases.""")
    test_case_specification: Optional[str] = Field(None, description="""Declarative specification of a set of Test Cases generated elsewhere (i.e. within a Test Runner)""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    

class Input(TestEntity):
    """
    Represents an input to a TestCase
    """
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    

class SemanticSmokeTestInput(Input):
    """
    Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.
    """
    must_pass_date: Optional[date] = Field(None, description="""The date by which this test must pass""")
    must_pass_environment: Optional[EnvironmentEnum] = Field(None, description="""The environment in which this test must pass""")
    query: Optional[str] = Field(None, description="""The question a SME would ask""")
    string_entry: Optional[str] = Field(None, description="""The object of the core triple to be tested""")
    direction: Optional[DirectionEnum] = Field(None, description="""The direction of the expected query result triple""")
    answer_informal_concept: Optional[str] = Field(None, description="""An answer that is returned from the test case, note: this must be combined with the expected_result to form a complete answer.  It might make sense to couple these in their own object instead of strictly sticking to the flat schema introduced by the spreadsheet here: https://docs.google.com/spreadsheets/d/1yj7zIchFeVl1OHqL_kE_pqvzNLmGml_FLbHDs-8Yvig/edit#gid=0""")
    expected_result: Optional[ExpectedResultsEnum] = Field(None, description="""The expected result of the query""")
    curie: Optional[str] = Field(None, description="""The curie of the query""")
    top_level: Optional[str] = Field(None, description="""The answer must return in these many results""")
    node: Optional[str] = Field(None, description="""The node of the TRAPI query to replace.""")
    notes: Optional[str] = Field(None, description="""The notes of the query""")
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    

class Output(TestEntity):
    """
    Represents an output from a TestCase
    """
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    

class SemanticSmokeTestOutput(Output):
    """
    Lifting schema from Shervin's runner JSON here as an example.  This schema is not yet complete.
    """
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    

class Precondition(TestEntity):
    """
    Represents a precondition for a TestCase
    """
    id: str = Field(..., description="""A unique identifier for a Test Entity""")
    name: Optional[str] = Field(None, description="""A human-readable name for a Test Entity""")
    description: Optional[str] = Field(None, description="""A human-readable description for a Test Entity""")
    tags: Optional[List[str]] = Field(default_factory=list, description="""A human-readable tags for categorical memberships of a TestEntity (preferably a URI or CURIE). Typically used to aggregate instances of TestEntity into formally typed or ad hoc lists.""")
    


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
TestEntity.model_rebuild()
TestMetadata.model_rebuild()
TestAsset.model_rebuild()
TestAssetCollection.model_rebuild()
QueryAnswerPair.model_rebuild()
TestEdgeData.model_rebuild()
TestCase.model_rebuild()
TestCaseSpecification.model_rebuild()
TestSuite.model_rebuild()
AcceptanceTestCase.model_rebuild()
AcceptanceTestSuite.model_rebuild()
BenchmarkTestSuite.model_rebuild()
StandardsComplianceTestSuite.model_rebuild()
OneHopTestSuite.model_rebuild()
Input.model_rebuild()
SemanticSmokeTestInput.model_rebuild()
Output.model_rebuild()
SemanticSmokeTestOutput.model_rebuild()
Precondition.model_rebuild()
    
