from tech_news.analyzer.reading_plan import ReadingPlanService
from unittest.mock import MagicMock
import pytest

mock = [
    {
        "url": "https://blog.guyddogl.com/tecnologia/frontend",
        "title": "React",
        "timestamp": "13/04/2023",
        "writer": "Guyddo",
        "reading_time": 6,
        "summary": "Uma tecnologia utilizada no front",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.guyddogl.com/tecnologia/backend",
        "title": "Node",
        "timestamp": "13/04/2023",
        "writer": "Guyddo",
        "reading_time": 5,
        "summary": "Uma tecnologia utilizada no back",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.guyddogl.com/tecnologia/fullstack",
        "title": "React + Node + SQL",
        "timestamp": "13/04/2023",
        "writer": "Guyddo",
        "reading_time": 17,
        "summary": "Serviço completo",
        "category": "Tecnologia",
    },
]


def test_reading_plan_group_news():
    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock)

    with pytest.raises(
        ValueError, match="'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-28)

    news = ReadingPlanService.group_news_for_available_time(7)

    assert len(news["readable"]) == 2
    assert len(news["unreadable"]) == 1
    assert news["readable"][0]["unfilled_time"] == 1
    assert news["readable"][1]["unfilled_time"] == 2
