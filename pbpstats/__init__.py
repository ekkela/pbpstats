import os

DATA_DIRECTORY = os.environ.get('PBP_STATS_DATA_DIRECTORY')
DATA_DIRECTORY is None
if DATA_DIRECTORY is not None and os.path.isdir(DATA_DIRECTORY):
    pbp_dir = f'{DATA_DIRECTORY}pbp/'
    game_details_dir = f'{DATA_DIRECTORY}game_details/'
    overrides_dir = f'{DATA_DIRECTORY}overrides/'
    if not os.path.isdir(pbp_dir):
        os.makedirs(pbp_dir)
    if not os.path.isdir(game_details_dir):
        os.makedirs(game_details_dir)
    if not os.path.isdir(overrides_dir):
        os.makedirs(overrides_dir)
else:
    DATA_DIRECTORY = None

VIDEO_EVENT_ASSET_BASE_URL = 'https://stats.nba.com/stats/videoeventsasset'
TODAYS_NBA_SCORES_URL = 'http://data.nba.com/data/5s/v2015/json/mobile_teams/nba/2019/scores/00_todays_scores.json'
TODAYS_WNBA_SCORES_URL = 'http://data.wnba.com/data/5s/v2015/json/mobile_teams/wnba/2019/scores/10_todays_scores.json'
TODAYS_G_LEAGUE_SCORES_URL = 'https://data.nba.com/data/10s/v2015/json/mobile_teams/dleague/2019/scores/20_todays_scores.json'
REQUEST_TIMEOUT = 10
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
REFERER = "http://stats.nba.com/"
HEADERS = {
    'User-Agent': USER_AGENT,
    'Referer': REFERER,
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}

NBA_STRING = 'nba'
G_LEAGUE_STRING = 'gleague'
WNBA_STRING = 'wnba'

NBA_GAME_ID_PREFIX = '00'
G_LEAGUE_GAME_ID_PREFIX = '20'
WNBA_GAME_ID_PREFIX = '10'

REGULAR_SEASON_STRING = 'Regular Season'
PLAYOFFS_STRING = 'Playoffs'

OFFENSIVE_ABBREVIATION_PREFIX = 'Off'
DEFENSIVE_ABBREVIATION_PREFIX = 'Def'
SECONDS_PLAYED_STRING = 'SecondsPlayed'
SECONDS_PLAYED_OFFENSE_STRING = f'{SECONDS_PLAYED_STRING}{OFFENSIVE_ABBREVIATION_PREFIX}'
SECONDS_PLAYED_DEFENSE_STRING = f'{SECONDS_PLAYED_STRING}{DEFENSIVE_ABBREVIATION_PREFIX}'
OFFENSIVE_POSSESSION_STRING = 'OffPoss'
DEFENSIVE_POSSESSION_STRING = 'DefPoss'
SECOND_CHANCE_STRING = 'SecondChance'
SECOND_CHANCE_SECONDS_PLAYED_OFFENSE_STRING = f'{SECOND_CHANCE_STRING}{SECONDS_PLAYED_OFFENSE_STRING}'
SECOND_CHANCE_SECONDS_PLAYED_DEFENSE_STRING = f'{SECOND_CHANCE_STRING}{SECONDS_PLAYED_DEFENSE_STRING}'

AT_RIM_CUTOFF = 4
SHORT_MID_RANGE_CUTOFF = 14
HEAVE_DISTANCE_CUTOFF = 40
HEAVE_TIME_CUTOFF = 2

TEAM_STAT_PLAYER_ID = '0'  # used as player id for team stats (ex team rebounds, shot clock violations)

AT_RIM_STRING = 'AtRim'
SHORT_MID_RANGE_STRING = 'ShortMidRange'
LONG_MID_RANGE_STRING = 'LongMidRange'
CORNER_3_STRING = 'Corner3'
ARC_3_STRING = 'Arc3'
UNKNOWN_SHOT_DISTANCE_STRING = 'UnknownDistance2pt'
FREE_THROW_STRING = 'FT'
FTS_MADE_STRING = 'FtsMade'
FT_1_PT_MADE_STRING = '1ptFtsMade'
FT_2_PT_MADE_STRING = '2ptFtsMade'
FT_3_PT_MADE_STRING = '3ptFtsMade'
ASSISTS_STRING = 'Assists'
REBOUNDS_STRING = 'Rebounds'
ASSISTED_STRING = 'Assisted'
UNASSISTED_STRING = 'Unassisted'
MISSED_STRING = 'Missed'
BLOCKED_STRING = 'Blocked'
REBOUND_OPPORTUNITIES_STRING = 'ReboundOpportunities'
REBOUNDED_STRING = 'Rebounded'
REBOUNDED_OPPORTUNITIES_STRING = 'ReboundedOpportunities'  # this is for getting oreb% on a player's missed shots
ON_FLOOR_OFFENSIVE_REBOUND_STRING = 'OnFloorOffReb'  # used for calculating player usage
BLOCK_STRING = 'Block'

PUTBACKS_STRING = 'Putbacks'
HEAVE_MISSES_STRING = 'HeaveMisses'
HEAVE_MAKES_STRING = 'HeaveMakes'

# attributes for shot data
SECONDS_SINCE_OREB_STRING = 'SecondsSinceOReb'
OREB_SHOT_PLAYER_ID_STRING = 'OrebShotPlayerId'
OREB_REBOUND_PLAYER_ID_STRING = 'OrebReboundPlayerId'
START_SCORE_DIFFERENTIAL_STRING = 'StartScoreDifferential'
SHOT_DISTANCE_STRING = 'ShotDistance'
SECONDS_SINCE_PLAY_STARTED = 'SecondsSincePlayStarted'
IS_REGULAR_SEASON_STRING = 'IsRegularSeason'
SHOT_ANGLE_STRING = 'ShotAngle'
PUTBACK_STRING = 'Putback'

MAKE_STRING = 'Make'
MISS_STRING = 'Miss'
MADE_STRING = 'Made'

SHOT_VALUE_STRING = 'ShotValue'
OPPONENT_POINTS = 'OpponentPoints'

PERSONAL_FOUL_TYPE_STRING = 'Personal Fouls'
SHOOTING_FOUL_TYPE_STRING = 'Shooting Fouls'
LOOSE_BALL_FOUL_TYPE_STRING = 'Loose Ball Fouls'
OFFENSIVE_FOUL_TYPE_STRING = 'Offensive Fouls'
AWAY_FROM_PLAY_FOUL_TYPE_STRING = 'Away From Play Fouls'
CHARGE_FOUL_TYPE_STRING = 'Charge Fouls'
PERSONAL_BLOCK_TYPE_STRING = 'Personal Block Fouls'
PERSONAL_TAKE_TYPE_STRING = 'Personal Take Fouls'
SHOOTING_BLOCK_TYPE_STRING = 'Shooting Block Fouls'
CLEAR_PATH_FOUL_TYPE_STRING = 'Clear Path Fouls'
DEFENSIVE_3_SECONDS_FOUL_TYPE_STRING = 'Defensive 3 Seconds Violations'
FLAGRANT_1_FOUL_TYPE_STRING = 'Flagrant 1 Fouls'
FLAGRANT_2_FOUL_TYPE_STRING = 'Flagrant 2 Fouls'
DOUBLE_FOUL_TYPE_STRING = 'Double Fouls'
INBOUND_FOUL_TYPE_STRING = 'Inbound Fouls'

FOULS_DRAWN_TYPE_STRING = ' Drawn'

OFF_DEADBALL_STRING = 'OffDeadball'
OFF_LIVE_BALL_TURNOVER_STRING = 'OffLiveBallTurnover'
OFF_TIMEOUT_STRING = 'OffTimeout'
OFF_MADE_FT_STRING = f'Off{FREE_THROW_STRING}{MAKE_STRING}'
OFF_MISSED_FT_STRING = f'Off{FREE_THROW_STRING}{MISS_STRING}'

PENALTY_STRING = 'Penalty'
FINAL_MINUTE_PENALTY_TAKE_FOUL_STRING = 'FinalMinutePenaltyTakeFoul'
PENALTY_POSSESSIONS_EXCLUDING_TAKE_FOUL_FTS = 'PenaltyOffPossExcludingTakeFouls'

PENALTY_FREE_THROW_STRING = 'Penalty Free Throw Trips'
THREE_POINT_AND1_FREE_THROW_STRING = '3pt And 1 Free Throw Trips'
TWO_POINT_AND1_FREE_THROW_STRING = '2pt And 1 Free Throw Trips'
THREE_POINT_SHOOTING_FOUL_FREE_THROW_STRING = '3pt Shooting Foul Free Throw Trips'
TWO_POINT_SHOOTING_FOUL_FREE_THROW_STRING = '2pt Shooting Foul Free Throw Trips'
TECHNICAL_FREE_THROW_STRING = 'Technical Free Throws Trips'

PLUS_MINUS_STRING = 'PlusMinus'
TIME_STRING = 'Time'

PLAYER_ID_STRING = 'PlayerId'
TEAM_ID_STRING = 'TeamId'
OPPONENT_TEAM_ID_STRING = 'OpponentTeamId'
LINEUP_ID_STRING = 'LineupId'
OPPONENT_LINEUP_ID_STRING = 'OpponentLineupId'

TOTAL_2PT_SHOT_DISTANCE_STRING = 'Total2ptShotDistance'
TOTAL_3PT_SHOT_DISTANCE_STRING = 'Total3ptShotDistance'
TOTAL_2PT_SHOTS_WITH_DISTANCE = 'Total2ptShotsWithDistance'
TOTAL_3PT_SHOTS_WITH_DISTANCE = 'Total3ptShotsWithDistance'

LIVEBALL_TURNOVERS_STRING = 'LiveBallTurnovers'
DEADBALL_TURNOVERS_STRING = 'DeadBallTurnovers'
STEALS_STRING = 'Steals'
TRAVELS_STRING = 'Travels'
THREE_SECOND_VIOLATION_TURNOVER_STRING = '3SecondViolations'
STEP_OUT_OF_BOUNDS_TURNOVER_STRING = 'StepOutOfBoundsTurnovers'
LOST_BALL_TURNOVER_STRING = 'LostBallTurnovers'
LOST_BALL_OUT_OF_BOUNDS_TURNOVER_STRING = 'LostBallOutOfBoundsTurnovers'
BAD_PASS_TURNOVER_STRING = 'BadPassTurnovers'
BAD_PASS_OUT_OF_BOUNDS_TURNOVER_STRING = 'BadPassOutOfBoundsTurnovers'

OFFENSIVE_GOALTENDING_STRING = 'OffensiveGoaltends'
DEFENSIVE_GOALTENDING_STRING = 'DefensiveGoaltends'

CHALLENGE_SUPPORT_RULING_STRING = 'ChallengeSupportRuling'
CHALLENGE_OVERTURN_RULING_STRING = 'ChallengeOverturnRuling'
CHALLENGE_RULING_STANDS_STRING = 'ChallengeRulingStands'

KEYS_OFF_BY_FACTOR_OF_5_WHEN_AGGREGATING_FOR_TEAM_AND_LINEUPS = [
    OFFENSIVE_POSSESSION_STRING,
    DEFENSIVE_POSSESSION_STRING,
    SECONDS_PLAYED_DEFENSE_STRING,
    SECONDS_PLAYED_OFFENSE_STRING,
    PLUS_MINUS_STRING,
    OPPONENT_POINTS,
    FREE_THROW_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    AT_RIM_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    SHORT_MID_RANGE_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    LONG_MID_RANGE_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    ARC_3_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    CORNER_3_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    AT_RIM_STRING + BLOCKED_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    SHORT_MID_RANGE_STRING + BLOCKED_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    LONG_MID_RANGE_STRING + BLOCKED_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    ARC_3_STRING + BLOCKED_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    CORNER_3_STRING + BLOCKED_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    FREE_THROW_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    AT_RIM_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    SHORT_MID_RANGE_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    LONG_MID_RANGE_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    ARC_3_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    CORNER_3_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    AT_RIM_STRING + BLOCKED_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    SHORT_MID_RANGE_STRING + BLOCKED_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    LONG_MID_RANGE_STRING + BLOCKED_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    ARC_3_STRING + BLOCKED_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    CORNER_3_STRING + BLOCKED_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    SECOND_CHANCE_STRING + OFFENSIVE_POSSESSION_STRING,
    SECOND_CHANCE_STRING + DEFENSIVE_POSSESSION_STRING,
    PENALTY_STRING + OFFENSIVE_POSSESSION_STRING,
    PENALTY_STRING + DEFENSIVE_POSSESSION_STRING,
    PENALTY_STRING + SECONDS_PLAYED_OFFENSE_STRING,
    PENALTY_STRING + SECONDS_PLAYED_DEFENSE_STRING,
    FINAL_MINUTE_PENALTY_TAKE_FOUL_STRING + OFFENSIVE_POSSESSION_STRING,
    FINAL_MINUTE_PENALTY_TAKE_FOUL_STRING + DEFENSIVE_POSSESSION_STRING,
    PENALTY_POSSESSIONS_EXCLUDING_TAKE_FOUL_FTS,
    PENALTY_STRING + FREE_THROW_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + AT_RIM_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + SHORT_MID_RANGE_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + LONG_MID_RANGE_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + ARC_3_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + CORNER_3_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + AT_RIM_STRING + BLOCKED_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + SHORT_MID_RANGE_STRING + BLOCKED_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + LONG_MID_RANGE_STRING + BLOCKED_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + ARC_3_STRING + BLOCKED_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + CORNER_3_STRING + BLOCKED_STRING + OFFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + FREE_THROW_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + AT_RIM_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + SHORT_MID_RANGE_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + LONG_MID_RANGE_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + ARC_3_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + CORNER_3_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + AT_RIM_STRING + BLOCKED_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + SHORT_MID_RANGE_STRING + BLOCKED_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + LONG_MID_RANGE_STRING + BLOCKED_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + ARC_3_STRING + BLOCKED_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
    PENALTY_STRING + CORNER_3_STRING + BLOCKED_STRING + DEFENSIVE_ABBREVIATION_PREFIX + REBOUND_OPPORTUNITIES_STRING,
]
