from utils.helpers import *
from config.paths_config import *


from pipeline.prediction_pipeline import hybrid_recommendation

print(hybrid_recommendation(3331))


# similar_users=find_similar_animes(313, USER_WEIGHTS_PATH, USER2USER_ENCODED, USER2USER_DECODED, DF)
# print(similar_users)
# user_pref = get_user_preferences(3331,RATING_DF,DF)
# print(user_pref)