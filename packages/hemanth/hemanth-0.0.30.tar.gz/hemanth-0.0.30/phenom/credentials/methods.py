from phenom.resumeparser.api.resume_parsing_api import ResumeParsingApi
from phenom.resumeparser.models.resume_request import ResumeRequest
from phenom.prediction.api.prediction_api import PredictionApi
from phenom.prediction.models.fyf_skill_request import FYFSkillRequest
class Methods():
    def __init__(self, token):
        self.token = token
    def parsebystream(self, file, description):
        request = ResumeRequest(file, description)
        return ResumeParsingApi().parse_by_stream(request.to_dict(), self.token)
    def skillsprediction(self, titles, skills, size, source):
        request = FYFSkillRequest(titles, skills, size, source)
        return PredictionApi().skills_prediction(request.to_dict(),self.token)