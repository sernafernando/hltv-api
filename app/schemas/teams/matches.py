from typing import Optional, List

from app.schemas.base import AuditMixin, HLTVBaseModel


# --- Shared ---

class MatchTeam(HLTVBaseModel):
    id: Optional[str] = None
    name: str
    url: Optional[str] = None


# --- Profile ---

class TeamProfileInfo(HLTVBaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    logo_url: Optional[str] = None
    country: Optional[str] = None
    country_flag_url: Optional[str] = None
    valve_ranking: Optional[str] = None
    world_ranking: Optional[str] = None
    weeks_in_top30: Optional[str] = None
    avg_player_age: Optional[str] = None


# --- Roster ---

class PlayerInfo(HLTVBaseModel):
    id: Optional[str] = None
    nickname: Optional[str] = None
    url: Optional[str] = None
    nationality: Optional[str] = None
    status: Optional[str] = None
    time_on_team: Optional[str] = None
    maps_played: Optional[str] = None
    rating: Optional[str] = None


class CoachInfo(HLTVBaseModel):
    id: Optional[str] = None
    nickname: Optional[str] = None
    url: Optional[str] = None
    time_on_team: Optional[str] = None
    maps_coached: Optional[str] = None
    trophies: Optional[str] = None
    winrate: Optional[str] = None


# --- Matches ---

class UpcomingMatch(HLTVBaseModel):
    date_unix: Optional[str] = None
    team1: MatchTeam
    team2: MatchTeam
    event_name: Optional[str] = None
    event_url: Optional[str] = None
    match_url: Optional[str] = None


class MatchResult(HLTVBaseModel):
    date_unix: Optional[str] = None
    team1: MatchTeam
    team1_score: Optional[str] = None
    team2: MatchTeam
    team2_score: Optional[str] = None
    event_name: Optional[str] = None
    event_url: Optional[str] = None
    match_url: Optional[str] = None


class TeamMatchStats(HLTVBaseModel):
    win_streak: Optional[str] = None
    win_rate: Optional[str] = None


# --- Events ---

class UpcomingEvent(HLTVBaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    start_date_unix: Optional[str] = None
    end_date_unix: Optional[str] = None


# --- Achievements ---

class Achievement(HLTVBaseModel):
    placement: Optional[str] = None
    tournament_name: Optional[str] = None
    tournament_url: Optional[str] = None


# --- Map Stats ---

class MapVeto(HLTVBaseModel):
    label: Optional[str] = None
    value: Optional[str] = None


class MapStatDetail(HLTVBaseModel):
    name: Optional[str] = None
    pick_ban_label: Optional[str] = None
    win_percentage: Optional[str] = None
    wins: Optional[str] = None
    draws: Optional[str] = None
    losses: Optional[str] = None
    round_win_after_first_kill: Optional[str] = None
    round_win_after_first_death: Optional[str] = None
    pistol_round_win_pct: Optional[str] = None
    veto: Optional[List[MapVeto]] = None


# --- Full Response ---

class TeamOverview(HLTVBaseModel, AuditMixin):
    id: str
    profile: Optional[TeamProfileInfo] = None
    coach: Optional[CoachInfo] = None
    players: Optional[List[PlayerInfo]] = None
    match_stats: Optional[TeamMatchStats] = None
    upcoming_count: int
    upcoming: List[UpcomingMatch]
    result_count: int
    results: List[MatchResult]
    upcoming_events: Optional[List[UpcomingEvent]] = None
    major_achievements: Optional[List[Achievement]] = None
    lan_achievements: Optional[List[Achievement]] = None
    map_stats: Optional[List[MapStatDetail]] = None
