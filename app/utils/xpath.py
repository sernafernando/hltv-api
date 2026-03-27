
class Players:
    class Profile:
        URL = "//link[@rel='canonical']//@href"
        NICKNAME = "//h1[@class='playerNickname']/text()"
        NAME = "//div[@class='playerRealname']/text()"
        AGE = "//div[@class='playerInfoRow playerAge']//span[@itemprop='text']/text()"
        NATIONALITY = "//div[@class='playerRealname']//img/@alt"
        RATING = "//div[@class='player-stat']//span[@class='statsVal']//p/text()"
        CURRENT_TEAM = "//div[@class='playerInfoRow playerTeam']//span[@class='listRight text-ellipsis']//span[@itemprop='text']//a/text()"
        CURRENT_TEAM_URL = "//div[@class='playerInfoRow playerTeam']//span[@class='listRight text-ellipsis']//a/@href"
        IMAGE_URL = "//img[@class = 'bodyshot-img']/@src"
        SOCIAL_MEDIA = "//div[@class = 'socialMediaButtons']//a/@href"

    class Search:
        FOUND = "//text()"
        BASE = "//table[@class='table'][.//td[@class='table-header'][contains(text(), 'Player')]]"
        RESULTS = BASE + "/tbody/tr[not(td[@class='table-header'])]"
        NAME = RESULTS + "/td/a/text()"
        URL = RESULTS +"/td/a/@href"
        NATIONALITY = RESULTS + "//img/@alt"

    class teamAchievements:
        ROWS = "//table[contains(@class, 'achievement-table')]//tr[contains(@class, 'team')]"
        PLACEMENT = ".//div[contains(@class, 'achievement')]/text()"
        TEAM_NAME = ".//td[contains(@class, 'team-name-cell')]//span[@class='team-name']/text()"
        TEAM_URL = ".//td[contains(@class, 'team-name-cell')]//a/@href"
        TOURNAMENT_NAME = ".//td[contains(@class, 'tournament-name-cell')]/a/text()"
        TOURNAMENT_URL = ".//td[contains(@class, 'tournament-name-cell')]/a/@href"
        PLAYER_STATS_URL = ".//td[contains(@class, 'stats-button-cell')]/a/@href"
    
    class personalAchievements:
        TOP_20_PLACEMENT = "//div[contains(@class,'playerTop20')]//span[contains(@class, 'top20ListRight')]/a/text()"
        TOP_20_YEAR = "//div[contains(@class,'playerTop20')]//span[contains(@class, 'top20ListRight')]/span/text()"
        TOP_20_ARTICLE_URL = "//div[contains(@class,'playerTop20')]//span[contains(@class, 'top20ListRight')]/a/@href"
        MAJOR_WINNER_COUNT = "//div[contains(@class, 'majorWinner')]/b"
        MAJOR_MVP_COUNT = "//div[contains(@class, 'majorMVP')]/b"
        MVP_WINNER_COUNT = "//div[contains(@class, 'mvp-count')]//text()"
        MVP_WINNER = "//div[contains(@class, 'trophyHolder')]//span[contains(@title, 'MVP')]/@title"
        EVP =  "//div[contains(@id, 'EVPs')]//tr[contains(@class,'trophy-row')]//div[contains(@class,'trophy-event')]/a/text()"
        

    class Trophies: 
        TOURNAMENT_NAME =  "//div[contains(@id, 'Trophies')]//tr[contains(@class, 'trophy-row')]//div[contains(@class, 'trophy-event')]/a/text()"
        TROPHY_IMG_URL = "//div[contains(@id, 'Trophies')]//tr[contains(@class, 'trophy-row')]//div[contains(@class, 'trophy-detail')]/img/@src"
        TOURNAMENT_URL = "//div[contains(@id, 'Trophies')]//tr[contains(@class, 'trophy-row')]//div[contains(@class, 'trophy-event')]/a/@href"
            
    class Stats: 
        #firepower stats
        KILLS_PER_ROUND = "//div[contains(@data-per-round-title, 'Kills per round') and not(contains(@data-per-round-title, 'Kills per round win')) and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        KILLS_PER_ROUND_WIN ="//div[contains(@data-per-round-title, 'Kills per round win') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        DAMAGE_PER_ROUND = "//div[contains(@data-per-round-title, 'Damage per round') and not(contains(@data-per-round-title, 'Damage per round win')) and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        DAMAGE_PER_ROUND_WIN ="//div[contains(@data-per-round-title, 'Damage per round win') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        ROUNDS_WITH_A_KILL_PERCENTAGE= "//div[contains(@data-per-round-title, 'Rounds with a kill') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        RATING_1_0 =  "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Rating 1.0')]]//div[contains(@class, 'role-stats-data')]/text()"
        ROUNDS_WITH_MULTI_KILL_PERCENTAGE = "//div[contains(@data-per-round-title, 'Rounds with a multi-kill') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        PISTOL_ROUND_RATING = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Pistol round rating')]]//div[contains(@class, 'role-stats-data')]/text()"
        
        #entrying stats
        SAVED_BY_TEAMMATE_PER_ROUND ="//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Saved by teammate per round')]]//div[contains(@class, 'role-stats-data')]/text()"
        TRADED_DEATHS_PER_ROUND = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Traded deaths per round')]]//div[contains(@class, 'role-stats-data')]/text()"
        TRADED_DEATHS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Traded deaths percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        OPENING_DEATHS_TRADED_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Opening deaths traded percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        ASSISTS_PER_ROUND = "//div[contains(@data-per-round-title, 'Assists per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        SUPPORT_ROUNDS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Support rounds')]]//div[contains(@class, 'role-stats-data')]/text()"
        
        #trading stats
        SAVED_TEAMMATE_PER_ROUND = "//div[contains(@data-per-round-title, 'Saved teammate per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        TRADE_KILLS_PER_ROUND = "//div[contains(@data-per-round-title, 'Trade kills per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        TRADE_KILLS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Trade kills percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        ASSISTED_KILLS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Assisted kills percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        DAMAGE_PER_KILL = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Damage per kill')]]//div[contains(@class, 'role-stats-data')]/text()"

        #opening stats
        OPENING_KILLS_PER_ROUND = "//div[contains(@data-per-round-title, 'Opening kills per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        OPENING_DEATHS_PER_ROUND = "//div[contains(@data-per-round-title, 'Opening deaths per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        OPENING_ATTEMPTS_PERCENTAGE = "//div[contains(@data-per-round-title, 'Opening attempts') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        OPENING_SUCCESS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Opening success')]]//div[contains(@class, 'role-stats-data')]/text()"
        WIN_AFTER_OPENING_KILL_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Win% after opening kill')]]//div[contains(@class, 'role-stats-data')]/text()"
        ATTACKS_PER_ROUND = "//div[contains(@data-per-round-title, 'Attacks per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"

        #clutching stats
        CLUTCH_POINTS_PER_ROUND = "//div[contains(@data-per-round-title, 'Clutch points per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        LAST_ALIVE_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Last alive percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        _1v1_WIN_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), '1on1 win percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        TIME_ALIVE_PER_ROUND = "//div[contains(@data-per-round-title, 'Time alive per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        SAVES_PER_ROUND_LOSS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Saves per round loss')]]//div[contains(@class, 'role-stats-data')]/text()"

        #sniping stats
        SNIPER_KILLS_PER_ROUND = "//div[contains(@data-per-round-title, 'Sniper kills per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        SNIPER_KILLS_PERCENTAGE = "//div[contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-top')][.//div[contains(@class, 'role-stats-title') and contains(text(), 'Sniper kills percentage')]]//div[contains(@class, 'role-stats-data')]/text()"
        ROUNDS_WITH_SNIPER_KILLS_PERCENTAGE = "//div[contains(@data-per-round-title, 'Rounds with sniper kills percentage') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        SNIPER_MULTI_KILL_ROUNDS = "//div[contains(@data-per-round-title, 'Sniper multi-kill rounds') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        SNIPER_OPENING_KILLS_PER_ROUND = "//div[contains(@data-per-round-title, 'Sniper opening kills per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"

        #utility stats
        UTILITY_DAMAGE_PER_ROUND = "//div[contains(@data-per-round-title, 'Utility damage per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        UTILITY_KILLS_PER_100_ROUNDS = "//div[contains(@data-per-round-title, 'Utility kills per 100 rounds') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        FLASHES_THROWN_PER_ROUND = "//div[contains(@data-per-round-title, 'Flashes thrown per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        FLASH_ASSISTS_PER_ROUND = "//div[contains(@data-per-round-title, 'Flash assists per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"
        TIME_OPPONENT_FLASHED_PER_ROUND ="//div[contains(@data-per-round-title, 'Time opponent flashed per round') and contains(@class, 'stats-side-combined')]//div[contains(@class, 'role-stats-data')]//text()"

    class careerStats:
        TOTAL_KILLS = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Total kills')]/following-sibling::span[1]/text()"
        HEADSHOT_PERCENTAGE = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Headshot %')]/following-sibling::span[1]/text()"
        TOTAL_DEATHS = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Total deaths')]/following-sibling::span[1]/text()"
        KD_RATIO = "//div[contains(@class, 'stats-row')]/span[contains(text(),'K/D Ratio')]/following-sibling::span[1]/text()"
        DAMAGE_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Damage / Round')]/following-sibling::span[1]/text()"
        GRENADE_DMG_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Grenade dmg / Round')]/following-sibling::span[1]/text()"
        MAPS_PLAYED = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Maps played')]/following-sibling::span[1]/text()"
        ROUNDS_PLAYED = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Rounds played')]/following-sibling::span[1]/text()"
        KILLS_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Kills / round')]/following-sibling::span[1]/text()"
        ASSISTS_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Assists / round')]/following-sibling::span[1]/text()"
        DEATHS_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Deaths / round')]/following-sibling::span[1]/text()"
        SAVED_BY_TEAMMATE_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Saved by teammate / round')]/following-sibling::span[1]/text()"
        SAVED_TEAMMATES_PER_ROUND = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Saved teammates / round')]/following-sibling::span[1]/text()"
        RATING1_0 = "//div[contains(@class, 'stats-row')]/span[contains(text(),'Rating 1.0')]/following-sibling::span[1]/text()"

class Events:
    class EventProfile:
        EVENT_URL = "//div[@class ='event-hub']//a/@href"
        EVENT_NAME = "//h1[contains(@class, 'event-hub-title')]/text()"
        TEAM_COUNT = "//td[contains(@class,'teamsNumber')]/text()"
        EVENT_START_DATE = "//th[contains(text(), 'Start date')]/parent::tr/td/span/text()"
        EVENT_END_DATE = "//th[contains(text(), 'End date')]/parent::tr/td/span/span/text()"
        PRIZE_POOL = "//td[contains(@class, 'prizepool')]/text()"
        PRIZE_CLUB_SHARE = "//th[contains(text(), 'Club share')]/following-sibling::td"
        PRIZE_PLAYER_SHARE = "//th[contains(text(), 'Player share')]/following-sibling::td"
        EVENT_LOCATION = "//td[contains(@class,'location')]//span/text()"
        LOCATION_FLAG_URL = "//td[contains(@class,'location')]//img/@src"
        MAP_POOL =  "//div[@class = 'map-pool-map-name']"

        #MVP
        EVENT_MVP_NICKNAME = "//div[@class= 'player-name']//a//span[@class = 'bold']/text()"
        EVENT_MVP_URL = "//div[@class= 'player-name']//a/@href"
        
        #EVPS
        EVENT_EVPS_NICKNAME = "//a[contains(@class, 'evp-wrapper')]//div[@class= 'evp-name-top']/text()"
        EVENT_EVPS_URL = "//a[contains(@class, 'evp-wrapper')]/@href"

        #teams       
        TEAM_NAME = "//div[@class='team-name']//div[@class='text-container']//div[@class='text']/text()"
        TEAM_URL = "//div[@class='team-name']//a/@href"
        TEAM_PLACEMENT = "//div[contains(@class,'placement')]/div[not(@class)]/text()"
        
    class EventTeamStats:

        #'teams attended' box
        TEAM_LINEUP = "//div[contains(@class, 'team-box') and .//a[contains(@href, '/team/{team_id}/')]]//div[contains(@class, 'lineup-box')]//div[contains(@class , 'flag-align player')]//text()"
        TEAM_PLAYER_URL = "//div[contains(@class, 'team-box') and .//a[contains(@href, '/team/{team_id}/')]]//div[contains(@class, 'lineup-box')]//div[contains(@class , 'flag-align player')]//a/@href"
        TEAM_COACH = "//div[contains(@class, 'team-box') and .//a[contains(@href, '/team/{team_id}/')]]//div[contains(@class,'coach-text')]/parent::div//div[contains(@class, 'flag-align player')]//text()"
        TEAM_COACH_URL = "//div[contains(@class, 'team-box') and .//a[contains(@href, '/team/{team_id}/')]]//div[contains(@class,'coach-text')]/parent::div//div[contains(@class, 'flag-align player')]//a/@href"
        QUALIFY_METHOD = "//div[contains(@class, 'team-box') and .//a[contains(@href, '/team/{team_id}/')]]//div[contains(@class, 'sub-text event-text')]//text()"
        
        
        #'vrs ranking' box
        VRS_DATE = "//th[contains(text(), 'VRS date')]/following-sibling::td//span"
        VRS_POINTS_BEFORE_EVENT = "//tbody[contains(@class, 'vrs-before')][.//a[contains(@href, '/team/{team_id}/')]]//tr[.//a[contains(@href, '/team/{team_id}/')]]/td[@class='vrs-points']/div[@class='start-only']//div"
        VRS_POINTS_AFTER_EVENT = "//tbody[contains(@class, 'vrs-after')][.//a[contains(@href, '/team/{team_id}/')]]//tr[.//a[contains(@href, '/team/{team_id}/')]]/td[@class='vrs-points']/div[@class='start-only']//div"
        VRS_POINTS_ACQUIRED = "//tbody[contains(@class, 'vrs-after')][.//a[contains(@href, '/team/{team_id}/')]]//tr[.//a[contains(@href, '/team/{team_id}/')]]/td[@class='vrs-points']/div[@class='finished-only']//div[contains(@class, 'finished-points')]"
        VRS_PLACEMENT_BEFORE_EVENT = "//tbody[contains(@class, 'vrs-before')][.//a[contains(@href, '/team/{team_id}/')]]//tr[.//a[contains(@href, '/team/{team_id}/')]]/td[@class = 'vrs-placements']//div[@class = 'start-only']//div[@class = 'vrs-placement-btn']"
        VRS_PLACEMENT_AFTER_EVENT = "//tbody[contains(@class, 'vrs-after')][.//a[contains(@href, '/team/{team_id}/')]]//tr[.//a[contains(@href, '/team/{team_id}/')]]/td[@class = 'vrs-placements']//div[@class = 'start-only']//div[@class = 'vrs-placement-btn']"

        
        #'prize distribution' box
        PRIZE = "//div[@class = 'team' and .//a[contains(@href,'/team/{team_id}/')]]/following-sibling::div[@class='prize']/text()"
        PRIZE_CLUB_SHARE = "//div[@class = 'team' and .//a[contains(@href,'/team/{team_id}/')]]/following-sibling::div[@class='prize club-share']/text()"
        TEAM_PLACEMENT  = "//div[@class = 'team' and .//a[contains(@href,'/team/{team_id}/')]]/following-sibling::div[not(@class)]/text()"


class Teams:
    class Profile:
        CANONICAL_URL = "//link[@rel='canonical']/@href"
        TEAM_NAME = "//h1/text()"
        LOGO_URL = "//div[contains(@class, 'profile-team')]//img/@src"
        COUNTRY = "//div[contains(@class, 'team-country')]//img/@alt"
        COUNTRY_FLAG_URL = "//div[contains(@class, 'team-country')]//img/@src"

        # info stats
        VALVE_RANKING = "//div[contains(@class, 'profile-team-stat')][.//b[text()='Valve ranking']]//a/text()"
        WORLD_RANKING = "//div[contains(@class, 'profile-team-stat')][.//b[text()='World ranking']]//a/text()"
        WEEKS_IN_TOP30 = "//div[contains(@class, 'profile-team-stat')][./b[text()='Weeks in top30 for core']]/span/text()"
        AVG_PLAYER_AGE = "//div[contains(@class, 'profile-team-stat')][./b[text()='Average player age']]/span/text()"

    class Roster:
        # players table
        PLAYER_ROWS = "//table[contains(@class, 'players-table')]//tbody//tr"
        PLAYER_NICK = ".//div[contains(@class, 'playersBox-playernick')]//div[@class='text-ellipsis']/text()"
        PLAYER_URL = ".//td[contains(@class, 'playersBox-first-cell')]//a/@href"
        PLAYER_STATUS = ".//td[2]//div/text()"
        PLAYER_TIME = ".//td[3]//div/text()"
        PLAYER_MAPS = ".//td[4]//div/text()"
        PLAYER_RATING = ".//td[last()]//div/text()"
        PLAYER_NATIONALITY = ".//img[contains(@class, 'flag')]/@alt"

        # coach table
        COACH_ROWS = "//table[contains(@class, 'coach-table')]//tbody//tr"
        COACH_NICK = ".//div[contains(@class, 'playersBox-playernick')]//div[@class='text-ellipsis']/text()"
        COACH_URL = ".//td[contains(@class, 'playersBox-first-cell')]//a/@href"
        COACH_TIME = ".//td[2]//div/text()"
        COACH_MAPS = ".//td[3]//div/text()"
        COACH_TROPHIES = ".//td[4]//div/text()"
        COACH_WINRATE = ".//td[5]//div/text()"

    class Matches:
        # highlighted stats
        WIN_STREAK = "//div[@id='matchesBox']//div[@class='highlighted-stat'][.//div[@class='description'][contains(text(), 'win streak')]]//div[@class='stat']/text()"
        WIN_RATE = "//div[@id='matchesBox']//div[@class='highlighted-stat'][.//div[@class='description'][contains(text(), 'Win rate')]]//div[@class='stat']/text()"

        # upcoming matches
        UPCOMING_ROWS = "//h2[contains(text(), 'Upcoming matches')]/following-sibling::table[1]//tr[@class='team-row']"

        # recent results
        RESULTS_ROWS = "//h2[contains(text(), 'Recent results')]/following-sibling::table//tr[@class='team-row']"

        # relative xpaths for each match row
        ROW_DATE_UNIX = ".//td[@class='date-cell']//span/@data-unix"
        ROW_TEAM1_NAME = ".//a[contains(@class, 'team-name team-1')]/text()"
        ROW_TEAM1_URL = ".//a[contains(@class, 'team-name team-1')]/@href"
        ROW_TEAM2_NAME = ".//a[contains(@class, 'team-name team-2')]/text()"
        ROW_TEAM2_URL = ".//a[contains(@class, 'team-name team-2')]/@href"
        ROW_SCORES = ".//div[contains(@class, 'score-cell')]//span[contains(@class, 'score') and not(contains(@class, 'divider'))]/text()"
        ROW_MATCH_URL = ".//td[contains(@class, 'button-cell')]//a/@href"
        ROW_EVENT_NAME = "./ancestor::table//tr[@class='event-header-cell']//a/text()"
        ROW_EVENT_URL = "./ancestor::table//tr[@class='event-header-cell']//a/@href"

    class UpcomingEvents:
        EVENT_ITEMS = "//div[@id='ongoingEvents']//a[contains(@class, 'ongoing-event')]"
        EVENT_NAME = ".//div[@class='eventbox-eventname']/text()"
        EVENT_URL = "@href"
        EVENT_DATES = ".//div[@class='eventbox-date']//span[@data-unix]/@data-unix"

    class Achievements:
        MAJOR_ROWS = "//div[@id='majorAchievement']//tr[@class='team']"
        LAN_ROWS = "//div[@id='lanAchievement']//tr[@class='team']"
        PLACEMENT = ".//div[contains(@class, 'achievement')]/text()"
        TOURNAMENT_NAME = ".//td[@class='tournament-name-cell']/a/text()"
        TOURNAMENT_URL = ".//td[@class='tournament-name-cell']/a/@href"

    class MapStats:
        MAP_CONTAINERS = "//div[@id='statsBox']//div[@class='map-statistics-container']"
        MAP_NAME = ".//div[@class='map-statistics-row-map-mapname']/text()"
        PICK_BAN_LABEL = ".//div[@class='pickban']/text()"
        WIN_PERCENTAGE = ".//div[@class='map-statistics-row-win-percentage']/text()"
        # W/D/L inside extended section
        WDL_STATS = ".//div[contains(@class, 'map-statistics-extended-wdl')]//div[@class='highlighted-stat']"
        WDL_VALUE = ".//div[@class='stat']/text()"
        WDL_LABEL = ".//div[@class='description']/text()"
        # general stats
        GENERAL_STATS = ".//div[@class='map-statistics-extended-general-stat']"
        GENERAL_STAT_LABEL = "./div[1]/text()"
        GENERAL_STAT_VALUE = "./div[2]/text()"
        # veto data
        VETO_ITEMS = ".//div[@class='map-statistics-extended-highlight-veto']"
        VETO_LABEL = "./div[1]/text()"
        VETO_VALUE = "./div[2]/text()"
