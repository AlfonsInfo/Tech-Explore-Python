from question import Question


class Utils:
    @staticmethod
    def map_array_of_dict_into_array_of_object(source, result):
        for index, question in enumerate(source):
            result.append(Question(question["text"], question["answer"]))
        return result
