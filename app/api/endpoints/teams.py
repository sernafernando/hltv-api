from fastapi import APIRouter

from app.schemas.teams.matches import TeamOverview
from app.services.teams.matches import HLTVTeamMatches

router = APIRouter()


@router.get("/{team_id}/overview", response_model=TeamOverview, response_model_exclude_none=True)
def get_team_overview(team_id: str):
    hltv = HLTVTeamMatches(team_id=team_id)
    return hltv.get_team_overview()
