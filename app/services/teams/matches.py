from dataclasses import dataclass

from app.services.base import HLTVBase
from app.utils.utils import trim, extract_from_url
from app.utils.xpath import Teams


@dataclass
class HLTVTeamMatches(HLTVBase):
    """
    Extracts all available data from a team's page in a single request:
    profile, roster, coach, matches, events, achievements, and map stats.

    Attributes:
        team_id (str): The HLTV team ID.
    """

    team_id: str

    def __post_init__(self) -> None:
        HLTVBase.__init__(self)
        url = f"https://www.hltv.org/team/{self.team_id}/a"
        self.URL = url
        self.page = self.request_url_page()

    # --- Profile ---

    def __parse_profile(self) -> dict:
        canonical = self.get_text_by_xpath(Teams.Profile.CANONICAL_URL)
        name = self.get_text_by_xpath(Teams.Profile.TEAM_NAME)
        logo_url = self.get_text_by_xpath(Teams.Profile.LOGO_URL)
        country = self.get_text_by_xpath(Teams.Profile.COUNTRY)
        country_flag = self.get_text_by_xpath(Teams.Profile.COUNTRY_FLAG_URL)
        valve_ranking = self.get_text_by_xpath(Teams.Profile.VALVE_RANKING)
        world_ranking = self.get_text_by_xpath(Teams.Profile.WORLD_RANKING)
        weeks_top30 = self.get_text_by_xpath(Teams.Profile.WEEKS_IN_TOP30)
        avg_age = self.get_text_by_xpath(Teams.Profile.AVG_PLAYER_AGE)

        return {
            "name": name,
            "url": canonical,
            "logo_url": logo_url,
            "country": country,
            "country_flag_url": f"https://www.hltv.org{country_flag}" if country_flag else None,
            "valve_ranking": valve_ranking,
            "world_ranking": world_ranking,
            "weeks_in_top30": weeks_top30,
            "avg_player_age": avg_age,
        }

    # --- Roster ---

    def __parse_players(self) -> list:
        rows = self.page.xpath(Teams.Roster.PLAYER_ROWS)
        players = []
        for row in rows:
            nick_list = row.xpath(Teams.Roster.PLAYER_NICK)
            nick = trim(nick_list[0]) if nick_list else None

            url_list = row.xpath(Teams.Roster.PLAYER_URL)
            url = url_list[0] if url_list else None
            player_id = extract_from_url(url, "id") if url else None

            nationality_list = row.xpath(Teams.Roster.PLAYER_NATIONALITY)
            nationality = trim(nationality_list[0]) if nationality_list else None

            status_list = row.xpath(Teams.Roster.PLAYER_STATUS)
            status = next((trim(s) for s in status_list if trim(s)), None)

            time_list = row.xpath(Teams.Roster.PLAYER_TIME)
            time_on = " ".join(trim(t) for t in time_list if trim(t)) if time_list else None

            maps_list = row.xpath(Teams.Roster.PLAYER_MAPS)
            maps = trim(maps_list[0]) if maps_list else None

            rating_list = row.xpath(Teams.Roster.PLAYER_RATING)
            rating = trim(rating_list[0]) if rating_list else None

            players.append({
                "id": player_id,
                "nickname": nick,
                "url": f"https://www.hltv.org{url}" if url else None,
                "nationality": nationality,
                "status": status,
                "time_on_team": time_on,
                "maps_played": maps,
                "rating": rating,
            })

        return players if players else None

    def __parse_coach(self) -> dict:
        rows = self.page.xpath(Teams.Roster.COACH_ROWS)
        if not rows:
            return None

        row = rows[0]
        nick_list = row.xpath(Teams.Roster.COACH_NICK)
        nick = trim(nick_list[0]) if nick_list else None

        url_list = row.xpath(Teams.Roster.COACH_URL)
        url = url_list[0] if url_list else None
        coach_id = extract_from_url(url, "id") if url else None

        time_list = row.xpath(Teams.Roster.COACH_TIME)
        time_on = " ".join(trim(t) for t in time_list if trim(t)) if time_list else None

        maps_list = row.xpath(Teams.Roster.COACH_MAPS)
        maps = trim(maps_list[0]) if maps_list else None

        trophies_list = row.xpath(Teams.Roster.COACH_TROPHIES)
        trophies = trim(trophies_list[0]) if trophies_list else None

        winrate_list = row.xpath(Teams.Roster.COACH_WINRATE)
        winrate = trim(winrate_list[0]) if winrate_list else None

        return {
            "id": coach_id,
            "nickname": nick,
            "url": f"https://www.hltv.org{url}" if url else None,
            "time_on_team": time_on,
            "maps_coached": maps,
            "trophies": trophies,
            "winrate": winrate,
        }

    # --- Matches ---

    def __parse_match_stats(self) -> dict:
        win_streak = self.get_text_by_xpath(Teams.Matches.WIN_STREAK)
        win_rate = self.get_text_by_xpath(Teams.Matches.WIN_RATE)

        if not win_streak and not win_rate:
            return None

        return {
            "win_streak": win_streak,
            "win_rate": win_rate,
        }

    def __parse_match_row(self, row) -> dict:
        date_unix_list = row.xpath(Teams.Matches.ROW_DATE_UNIX)
        date_unix = date_unix_list[0] if date_unix_list else None

        team1_name_list = row.xpath(Teams.Matches.ROW_TEAM1_NAME)
        team1_name = trim(team1_name_list[0]) if team1_name_list else None

        team1_url_list = row.xpath(Teams.Matches.ROW_TEAM1_URL)
        team1_url = team1_url_list[0] if team1_url_list else None
        team1_id = extract_from_url(team1_url, "id") if team1_url else None

        team2_name_list = row.xpath(Teams.Matches.ROW_TEAM2_NAME)
        team2_name = trim(team2_name_list[0]) if team2_name_list else None

        team2_url_list = row.xpath(Teams.Matches.ROW_TEAM2_URL)
        team2_url = team2_url_list[0] if team2_url_list else None
        team2_id = extract_from_url(team2_url, "id") if team2_url else None

        scores = row.xpath(Teams.Matches.ROW_SCORES)

        match_url_list = row.xpath(Teams.Matches.ROW_MATCH_URL)
        match_url = f"https://www.hltv.org{match_url_list[0]}" if match_url_list else None

        event_name_list = row.xpath(Teams.Matches.ROW_EVENT_NAME)
        event_name = trim(event_name_list[0]) if event_name_list else None

        event_url_list = row.xpath(Teams.Matches.ROW_EVENT_URL)
        event_url = f"https://www.hltv.org{event_url_list[0]}" if event_url_list else None

        return {
            "date_unix": date_unix,
            "team1": {
                "id": team1_id,
                "name": team1_name,
                "url": f"https://www.hltv.org{team1_url}" if team1_url else None,
            },
            "team1_score": trim(scores[0]) if len(scores) > 0 and scores[0].strip() != "-" else None,
            "team2": {
                "id": team2_id,
                "name": team2_name,
                "url": f"https://www.hltv.org{team2_url}" if team2_url else None,
            },
            "team2_score": trim(scores[1]) if len(scores) > 1 and scores[1].strip() != "-" else None,
            "event_name": event_name,
            "event_url": event_url,
            "match_url": match_url,
        }

    # --- Events ---

    def __parse_upcoming_events(self) -> list:
        items = self.page.xpath(Teams.UpcomingEvents.EVENT_ITEMS)
        events = []
        for item in items:
            name_list = item.xpath(Teams.UpcomingEvents.EVENT_NAME)
            name = trim(name_list[0]) if name_list else None

            url_list = item.xpath(Teams.UpcomingEvents.EVENT_URL)
            url = f"https://www.hltv.org{url_list[0]}" if url_list else None

            dates = item.xpath(Teams.UpcomingEvents.EVENT_DATES)

            events.append({
                "name": name,
                "url": url,
                "start_date_unix": dates[0] if len(dates) > 0 else None,
                "end_date_unix": dates[1] if len(dates) > 1 else None,
            })

        return events if events else None

    # --- Achievements ---

    def __parse_achievements(self, xpath_rows: str) -> list:
        rows = self.page.xpath(xpath_rows)
        achievements = []
        for row in rows:
            placement_list = row.xpath(Teams.Achievements.PLACEMENT)
            placement = trim(placement_list[0]) if placement_list else None

            name_list = row.xpath(Teams.Achievements.TOURNAMENT_NAME)
            name = trim(name_list[0]) if name_list else None

            url_list = row.xpath(Teams.Achievements.TOURNAMENT_URL)
            url = f"https://www.hltv.org{url_list[0]}" if url_list else None

            achievements.append({
                "placement": placement,
                "tournament_name": name,
                "tournament_url": url,
            })

        return achievements if achievements else None

    # --- Map Stats ---

    def __parse_map_stats(self) -> list:
        containers = self.page.xpath(Teams.MapStats.MAP_CONTAINERS)
        maps = []
        for mc in containers:
            name_list = mc.xpath(Teams.MapStats.MAP_NAME)
            name = trim(name_list[0]) if name_list else None

            pick_ban_list = mc.xpath(Teams.MapStats.PICK_BAN_LABEL)
            pick_ban = trim(pick_ban_list[0]) if pick_ban_list else None

            win_pct_list = mc.xpath(Teams.MapStats.WIN_PERCENTAGE)
            win_pct = trim(win_pct_list[0]) if win_pct_list else None

            # W/D/L
            wdl_items = mc.xpath(Teams.MapStats.WDL_STATS)
            wins = draws = losses = None
            for item in wdl_items:
                val = item.xpath(Teams.MapStats.WDL_VALUE)
                label = item.xpath(Teams.MapStats.WDL_LABEL)
                if val and label:
                    v = trim(val[0])
                    l = trim(label[0]).lower()
                    if "win" in l:
                        wins = v
                    elif "draw" in l:
                        draws = v
                    elif "loss" in l:
                        losses = v

            # General stats
            gen_items = mc.xpath(Teams.MapStats.GENERAL_STATS)
            rw_first_kill = rw_first_death = pistol_pct = None
            for item in gen_items:
                label = item.xpath(Teams.MapStats.GENERAL_STAT_LABEL)
                value = item.xpath(Teams.MapStats.GENERAL_STAT_VALUE)
                if label and value:
                    l = trim(label[0]).lower()
                    v = trim(value[0])
                    if "first kill" in l:
                        rw_first_kill = v
                    elif "first death" in l:
                        rw_first_death = v
                    elif "pistol" in l:
                        pistol_pct = v

            # Veto
            veto_items = mc.xpath(Teams.MapStats.VETO_ITEMS)
            veto = []
            for item in veto_items:
                vl = item.xpath(Teams.MapStats.VETO_LABEL)
                vv = item.xpath(Teams.MapStats.VETO_VALUE)
                if vl and vv:
                    veto.append({"label": trim(vl[0]), "value": trim(vv[0])})

            maps.append({
                "name": name,
                "pick_ban_label": pick_ban,
                "win_percentage": win_pct,
                "wins": wins,
                "draws": draws,
                "losses": losses,
                "round_win_after_first_kill": rw_first_kill,
                "round_win_after_first_death": rw_first_death,
                "pistol_round_win_pct": pistol_pct,
                "veto": veto if veto else None,
            })

        return maps if maps else None

    # --- Public API ---

    def get_team_overview(self) -> dict:
        """Single request, all data."""
        upcoming_rows = self.page.xpath(Teams.Matches.UPCOMING_ROWS)
        upcoming = [self.__parse_match_row(row) for row in upcoming_rows]

        results_rows = self.page.xpath(Teams.Matches.RESULTS_ROWS)
        results = [self.__parse_match_row(row) for row in results_rows]

        self.response["id"] = self.team_id
        self.response["profile"] = self.__parse_profile()
        self.response["coach"] = self.__parse_coach()
        self.response["players"] = self.__parse_players()
        self.response["match_stats"] = self.__parse_match_stats()
        self.response["upcoming_count"] = len(upcoming)
        self.response["upcoming"] = upcoming
        self.response["result_count"] = len(results)
        self.response["results"] = results
        self.response["upcoming_events"] = self.__parse_upcoming_events()
        self.response["major_achievements"] = self.__parse_achievements(Teams.Achievements.MAJOR_ROWS)
        self.response["lan_achievements"] = self.__parse_achievements(Teams.Achievements.LAN_ROWS)
        self.response["map_stats"] = self.__parse_map_stats()

        return self.response
