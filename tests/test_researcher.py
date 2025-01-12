"""Tests for the main researcher class."""

import pytest
from researcher.core.researcher import Researcher, ResearchResult


@pytest.fixture
def researcher():
    """Create a researcher instance for testing."""
    return Researcher()


async def test_research_creation(researcher):
    """Test that researcher instance is created properly."""
    assert researcher.results == []


async def test_research_query(researcher):
    """Test basic research functionality."""
    results = await researcher.research("test query")
    assert isinstance(results, list)
    

async def test_summarize(researcher):
    """Test summarization functionality."""
    summary = await researcher.summarize()
    assert isinstance(summary, str)
