class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # 
        lang_cnt = len(languages)
        cant_communicate = set()
        for friend1, friend2 in friendships:
            friend1 -= 1
            friend2 -= 1
            # if they can't communicate, add them to the set
            if not (set(languages[friend1]) & set(languages[friend2])):
                cant_communicate.add(friend1)
                cant_communicate.add(friend2)

        needs_teaching = len(cant_communicate)
        unknown_languages = [needs_teaching]*n
        # now that we have a list of all those who can't communicate, figure out the easiest way to make all them connumicate
        for language_learner in cant_communicate:
            for lang in languages[language_learner]:
                unknown_languages[lang - 1] -= 1
        
        # now we have a list of every language we can teach, now return the minimum of that array
        return min(unknown_languages)

