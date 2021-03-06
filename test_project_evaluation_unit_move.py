import wargroove_ctrl
import cmp504
import unit_constants
import unittest
from assertpy import assert_that


class TestProjectEvaluationUnitMove(unittest.TestCase):

    @staticmethod
    def __get_eval_folder():
        return 'data/evaluation-frames/units-and-buildings/moving-targets/'

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERCIA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_mercia_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(122)
        assert_that(match.bottom_right[0]).is_equal_to(392)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_1_mercia_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(122)
        assert_that(match.bottom_right[0]).is_equal_to(392)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_1_mercia_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(122)
        assert_that(match.bottom_right[0]).is_equal_to(392)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_1_mercia_sift(self):
        threshold = unit_constants.cherrystone_mercia_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_mercia',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(354, 392)
        assert_that(match.location[1]).is_between(122, 176)

    def test_frame_2_mercia_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(882)
        assert_that(match.top_left[1]).is_equal_to(122)
        assert_that(match.bottom_right[0]).is_equal_to(920)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_2_mercia_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(882)
        assert_that(match.top_left[1]).is_equal_to(122)
        assert_that(match.bottom_right[0]).is_equal_to(920)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_2_mercia_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_mercia_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_mercia',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(882)
        assert_that(match.top_left[1]).is_equal_to(122)
        assert_that(match.bottom_right[0]).is_equal_to(920)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_2_mercia_sift(self):
        threshold = unit_constants.cherrystone_mercia_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_mercia',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(882, 920)
        assert_that(match.location[1]).is_between(122, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- EMERIC ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_emeric_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(360)
        assert_that(match.top_left[1]).is_equal_to(220)
        assert_that(match.bottom_right[0]).is_equal_to(390)
        assert_that(match.bottom_right[1]).is_equal_to(274)

    def test_frame_1_emeric_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(360)
        assert_that(match.top_left[1]).is_equal_to(220)
        assert_that(match.bottom_right[0]).is_equal_to(390)
        assert_that(match.bottom_right[1]).is_equal_to(274)

    def test_frame_1_emeric_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(360)
        assert_that(match.top_left[1]).is_equal_to(220)
        assert_that(match.bottom_right[0]).is_equal_to(390)
        assert_that(match.bottom_right[1]).is_equal_to(274)

    def test_frame_1_emeric_sift(self):
        threshold = unit_constants.cherrystone_emeric_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_emeric',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(360, 390)
        assert_that(match.location[1]).is_between(220, 274)

    def test_frame_2_emeric_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(888)
        assert_that(match.top_left[1]).is_equal_to(220)
        assert_that(match.bottom_right[0]).is_equal_to(918)
        assert_that(match.bottom_right[1]).is_equal_to(274)

    def test_frame_2_emeric_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(888)
        assert_that(match.top_left[1]).is_equal_to(220)
        assert_that(match.bottom_right[0]).is_equal_to(918)
        assert_that(match.bottom_right[1]).is_equal_to(274)

    def test_frame_2_emeric_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_emeric_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_emeric',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(888)
        assert_that(match.top_left[1]).is_equal_to(220)
        assert_that(match.bottom_right[0]).is_equal_to(918)
        assert_that(match.bottom_right[1]).is_equal_to(274)

    def test_frame_2_emeric_sift(self):
        threshold = unit_constants.cherrystone_emeric_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_emeric',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(888, 918)
        assert_that(match.location[1]).is_between(220, 274)

    # ----------------------------------------------------------------------------
    # ---------------------------------- CAESAR ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_caesar_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(404)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_1_caesar_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(404)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_1_caesar_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(354)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(404)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_1_caesar_sift(self):
        threshold = unit_constants.cherrystone_caesar_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_caesar',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(354, 404)
        assert_that(match.location[1]).is_between(320, 368)

    def test_frame_2_caesar_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(882)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(932)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_2_caesar_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(882)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(932)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_2_caesar_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_caesar_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_commander_caesar',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(882)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(932)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_2_caesar_sift(self):
        threshold = unit_constants.cherrystone_caesar_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_commander_caesar',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(882, 932)
        assert_that(match.location[1]).is_between(320, 368)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_villager_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(506)
        assert_that(match.top_left[1]).is_equal_to(124)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_1_villager_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(506)
        assert_that(match.top_left[1]).is_equal_to(124)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_1_villager_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(506)
        assert_that(match.top_left[1]).is_equal_to(124)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_1_villager_sift(self):
        threshold = unit_constants.cherrystone_villager_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_villager',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(506, 536)
        assert_that(match.location[1]).is_between(124, 176)

    def test_frame_2_villager_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(746)
        assert_that(match.top_left[1]).is_equal_to(124)
        assert_that(match.bottom_right[0]).is_equal_to(776)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_2_villager_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(746)
        assert_that(match.top_left[1]).is_equal_to(124)
        assert_that(match.bottom_right[0]).is_equal_to(776)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_2_villager_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_villager_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_villager',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(746)
        assert_that(match.top_left[1]).is_equal_to(124)
        assert_that(match.bottom_right[0]).is_equal_to(776)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_2_villager_sift(self):
        threshold = unit_constants.cherrystone_villager_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_villager',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(746, 776)
        assert_that(match.location[1]).is_between(124, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SOLDIER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_soldier_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(500)
        assert_that(match.top_left[1]).is_equal_to(218)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_1_soldier_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(500)
        assert_that(match.top_left[1]).is_equal_to(218)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_1_soldier_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(500)
        assert_that(match.top_left[1]).is_equal_to(218)
        assert_that(match.bottom_right[0]).is_equal_to(536)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_1_soldier_sift(self):
        threshold = unit_constants.cherrystone_soldier_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_soldier',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(500, 536)
        assert_that(match.location[1]).is_between(218, 272)

    def test_frame_2_soldier_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(740)
        assert_that(match.top_left[1]).is_equal_to(218)
        assert_that(match.bottom_right[0]).is_equal_to(776)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_2_soldier_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(740)
        assert_that(match.top_left[1]).is_equal_to(218)
        assert_that(match.bottom_right[0]).is_equal_to(776)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_2_soldier_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_soldier_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_soldier',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(740)
        assert_that(match.top_left[1]).is_equal_to(218)
        assert_that(match.bottom_right[0]).is_equal_to(776)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_2_soldier_sift(self):
        threshold = unit_constants.cherrystone_soldier_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_soldier',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(740, 776)
        assert_that(match.location[1]).is_between(218, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PIKEMAN ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_pikeman_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(502)
        assert_that(match.top_left[1]).is_equal_to(324)
        assert_that(match.bottom_right[0]).is_equal_to(554)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_1_pikeman_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(502)
        assert_that(match.top_left[1]).is_equal_to(324)
        assert_that(match.bottom_right[0]).is_equal_to(554)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_1_pikeman_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(502)
        assert_that(match.top_left[1]).is_equal_to(324)
        assert_that(match.bottom_right[0]).is_equal_to(554)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_1_pikeman_sift(self):
        threshold = unit_constants.cherrystone_pikeman_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_pikeman',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(502, 554)
        assert_that(match.location[1]).is_between(324, 368)

    def test_frame_2_pikeman_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(742)
        assert_that(match.top_left[1]).is_equal_to(324)
        assert_that(match.bottom_right[0]).is_equal_to(794)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_2_pikeman_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(742)
        assert_that(match.top_left[1]).is_equal_to(324)
        assert_that(match.bottom_right[0]).is_equal_to(794)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_2_pikeman_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_pikeman_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_pikeman',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(742)
        assert_that(match.top_left[1]).is_equal_to(324)
        assert_that(match.bottom_right[0]).is_equal_to(794)
        assert_that(match.bottom_right[1]).is_equal_to(368)

    def test_frame_2_pikeman_sift(self):
        threshold = unit_constants.cherrystone_pikeman_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_pikeman',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(742, 794)
        assert_that(match.location[1]).is_between(324, 368)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BATTLEPUP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_battlepup_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(596)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(642)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_1_battlepup_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(596)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(642)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_1_battlepup_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(596)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(642)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_1_battlepup_sift(self):
        threshold = unit_constants.cherrystone_battlepup_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_battle_pup',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(596, 642)
        assert_that(match.location[1]).is_between(138, 176)

    def test_frame_2_battlepup_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(644)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_2_battlepup_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(644)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_2_battlepup_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_battlepup_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_battle_pup',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(644)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(176)

    def test_frame_2_battlepup_sift(self):
        threshold = unit_constants.cherrystone_battlepup_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_battle_pup',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(644, 690)
        assert_that(match.location[1]).is_between(138, 176)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ALCHEMIST ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_alchemist_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(222)
        assert_that(match.bottom_right[0]).is_equal_to(636)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_1_alchemist_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(222)
        assert_that(match.bottom_right[0]).is_equal_to(636)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_1_alchemist_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(592)
        assert_that(match.top_left[1]).is_equal_to(222)
        assert_that(match.bottom_right[0]).is_equal_to(636)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_1_alchemist_sift(self):
        threshold = unit_constants.cherrystone_alchemist_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_alchemist',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(592, 636)
        assert_that(match.location[1]).is_between(222, 272)

    def test_frame_2_alchemist_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(640)
        assert_that(match.top_left[1]).is_equal_to(222)
        assert_that(match.bottom_right[0]).is_equal_to(684)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_2_alchemist_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(640)
        assert_that(match.top_left[1]).is_equal_to(222)
        assert_that(match.bottom_right[0]).is_equal_to(684)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_2_alchemist_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_alchemist_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_alchemist',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(640)
        assert_that(match.top_left[1]).is_equal_to(222)
        assert_that(match.bottom_right[0]).is_equal_to(684)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_2_alchemist_sift(self):
        threshold = unit_constants.cherrystone_alchemist_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_alchemist',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(640, 684)
        assert_that(match.location[1]).is_between(222, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- ARCHER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_archer_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(590)
        assert_that(match.top_left[1]).is_equal_to(314)
        assert_that(match.bottom_right[0]).is_equal_to(634)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_1_archer_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(590)
        assert_that(match.top_left[1]).is_equal_to(314)
        assert_that(match.bottom_right[0]).is_equal_to(634)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_1_archer_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(590)
        assert_that(match.top_left[1]).is_equal_to(314)
        assert_that(match.bottom_right[0]).is_equal_to(634)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_1_archer_sift(self):
        threshold = unit_constants.cherrystone_archer_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_archer',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(590, 634)
        assert_that(match.location[1]).is_between(314, 370)

    def test_frame_2_archer_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(638)
        assert_that(match.top_left[1]).is_equal_to(314)
        assert_that(match.bottom_right[0]).is_equal_to(682)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_2_archer_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(638)
        assert_that(match.top_left[1]).is_equal_to(314)
        assert_that(match.bottom_right[0]).is_equal_to(682)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_2_archer_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_archer_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_archer',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(638)
        assert_that(match.top_left[1]).is_equal_to(314)
        assert_that(match.bottom_right[0]).is_equal_to(682)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_2_archer_sift(self):
        threshold = unit_constants.cherrystone_archer_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_archer',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(638, 682)
        assert_that(match.location[1]).is_between(314, 370)

    # ----------------------------------------------------------------------------
    # ---------------------------------- GOLEM ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_golem_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(692)
        assert_that(match.top_left[1]).is_equal_to(108)
        assert_that(match.bottom_right[0]).is_equal_to(732)
        assert_that(match.bottom_right[1]).is_equal_to(178)

    def test_frame_1_golem_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(692)
        assert_that(match.top_left[1]).is_equal_to(108)
        assert_that(match.bottom_right[0]).is_equal_to(732)
        assert_that(match.bottom_right[1]).is_equal_to(178)

    def test_frame_1_golem_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(692)
        assert_that(match.top_left[1]).is_equal_to(108)
        assert_that(match.bottom_right[0]).is_equal_to(732)
        assert_that(match.bottom_right[1]).is_equal_to(178)

    def test_frame_1_golem_sift(self):
        threshold = unit_constants.cherrystone_golem_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_golem',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(692, 732)
        assert_that(match.location[1]).is_between(108, 178)

    def test_frame_2_golem_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(548)
        assert_that(match.top_left[1]).is_equal_to(108)
        assert_that(match.bottom_right[0]).is_equal_to(588)
        assert_that(match.bottom_right[1]).is_equal_to(178)

    def test_frame_2_golem_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(548)
        assert_that(match.top_left[1]).is_equal_to(108)
        assert_that(match.bottom_right[0]).is_equal_to(588)
        assert_that(match.bottom_right[1]).is_equal_to(178)

    def test_frame_2_golem_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_golem_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_golem',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(548)
        assert_that(match.top_left[1]).is_equal_to(108)
        assert_that(match.bottom_right[0]).is_equal_to(588)
        assert_that(match.bottom_right[1]).is_equal_to(178)

    def test_frame_2_golem_sift(self):
        threshold = unit_constants.cherrystone_golem_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_golem',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(548, 588)
        assert_that(match.location[1]).is_between(108, 178)

    # ----------------------------------------------------------------------------
    # ---------------------------------- KNIGHT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_knight_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(693)
        assert_that(match.top_left[1]).is_equal_to(208)
        assert_that(match.bottom_right[0]).is_equal_to(744)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_1_knight_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(693)
        assert_that(match.top_left[1]).is_equal_to(208)
        assert_that(match.bottom_right[0]).is_equal_to(744)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_1_knight_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(693)
        assert_that(match.top_left[1]).is_equal_to(208)
        assert_that(match.bottom_right[0]).is_equal_to(744)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_1_knight_sift(self):
        threshold = unit_constants.cherrystone_knight_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_knight',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(693, 744)
        assert_that(match.location[1]).is_between(208, 272)

    def test_frame_2_knight_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(549)
        assert_that(match.top_left[1]).is_equal_to(208)
        assert_that(match.bottom_right[0]).is_equal_to(600)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_2_knight_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(549)
        assert_that(match.top_left[1]).is_equal_to(208)
        assert_that(match.bottom_right[0]).is_equal_to(600)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_2_knight_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_knight_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_knight',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(549)
        assert_that(match.top_left[1]).is_equal_to(208)
        assert_that(match.bottom_right[0]).is_equal_to(600)
        assert_that(match.bottom_right[1]).is_equal_to(272)

    def test_frame_2_knight_sift(self):
        threshold = unit_constants.cherrystone_knight_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_knight',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(549, 600)
        assert_that(match.location[1]).is_between(208, 272)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_wagon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(686)
        assert_that(match.top_left[1]).is_equal_to(319)
        assert_that(match.bottom_right[0]).is_equal_to(742)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_1_wagon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(686)
        assert_that(match.top_left[1]).is_equal_to(319)
        assert_that(match.bottom_right[0]).is_equal_to(742)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_1_wagon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(686)
        assert_that(match.top_left[1]).is_equal_to(319)
        assert_that(match.bottom_right[0]).is_equal_to(742)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_1_wagon_sift(self):
        threshold = unit_constants.cherrystone_wagon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_wagon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(686, 742)
        assert_that(match.location[1]).is_between(319, 370)

    def test_frame_2_wagon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(542)
        assert_that(match.top_left[1]).is_equal_to(319)
        assert_that(match.bottom_right[0]).is_equal_to(598)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_2_wagon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(542)
        assert_that(match.top_left[1]).is_equal_to(319)
        assert_that(match.bottom_right[0]).is_equal_to(598)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_2_wagon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_wagon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_wagon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(542)
        assert_that(match.top_left[1]).is_equal_to(319)
        assert_that(match.bottom_right[0]).is_equal_to(598)
        assert_that(match.bottom_right[1]).is_equal_to(370)

    def test_frame_2_wagon_sift(self):
        threshold = unit_constants.cherrystone_wagon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_wagon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(542, 598)
        assert_that(match.location[1]).is_between(319, 370)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLISTA ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_ballista_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(842)
        assert_that(match.bottom_right[1]).is_equal_to(180)

    def test_frame_1_ballista_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(842)
        assert_that(match.bottom_right[1]).is_equal_to(180)

    def test_frame_1_ballista_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(842)
        assert_that(match.bottom_right[1]).is_equal_to(180)

    def test_frame_1_ballista_sift(self):
        threshold = unit_constants.cherrystone_ballista_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_ballista',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(782, 842)
        assert_that(match.location[1]).is_between(138, 180)

    def test_frame_2_ballista_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(506)
        assert_that(match.bottom_right[1]).is_equal_to(180)

    def test_frame_2_ballista_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(506)
        assert_that(match.bottom_right[1]).is_equal_to(180)

    def test_frame_2_ballista_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_ballista_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_ballista',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(138)
        assert_that(match.bottom_right[0]).is_equal_to(506)
        assert_that(match.bottom_right[1]).is_equal_to(180)

    def test_frame_2_ballista_sift(self):
        threshold = unit_constants.cherrystone_ballista_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_ballista',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(446, 506)
        assert_that(match.location[1]).is_between(138, 180)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TREBUCHET ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_trebuchet_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(226)
        assert_that(match.bottom_right[0]).is_equal_to(844)
        assert_that(match.bottom_right[1]).is_equal_to(276)

    def test_frame_1_trebuchet_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(226)
        assert_that(match.bottom_right[0]).is_equal_to(844)
        assert_that(match.bottom_right[1]).is_equal_to(276)

    def test_frame_1_trebuchet_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(782)
        assert_that(match.top_left[1]).is_equal_to(226)
        assert_that(match.bottom_right[0]).is_equal_to(844)
        assert_that(match.bottom_right[1]).is_equal_to(276)

    def test_frame_1_trebuchet_sift(self):
        threshold = unit_constants.cherrystone_trebuchet_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_trebuchet',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(782, 844)
        assert_that(match.location[1]).is_between(226, 276)

    def test_frame_2_trebuchet_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(226)
        assert_that(match.bottom_right[0]).is_equal_to(508)
        assert_that(match.bottom_right[1]).is_equal_to(276)

    def test_frame_2_trebuchet_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(226)
        assert_that(match.bottom_right[0]).is_equal_to(508)
        assert_that(match.bottom_right[1]).is_equal_to(276)

    def test_frame_2_trebuchet_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_trebuchet_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_trebuchet',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(226)
        assert_that(match.bottom_right[0]).is_equal_to(508)
        assert_that(match.bottom_right[1]).is_equal_to(276)

    def test_frame_2_trebuchet_sift(self):
        threshold = unit_constants.cherrystone_trebuchet_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_trebuchet',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(446, 508)
        assert_that(match.location[1]).is_between(226, 276)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BALLOON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_balloon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(770)
        assert_that(match.top_left[1]).is_equal_to(300)
        assert_that(match.bottom_right[0]).is_equal_to(830)
        assert_that(match.bottom_right[1]).is_equal_to(362)

    def test_frame_1_balloon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(770)
        assert_that(match.top_left[1]).is_equal_to(300)
        assert_that(match.bottom_right[0]).is_equal_to(830)
        assert_that(match.bottom_right[1]).is_equal_to(362)

    def test_frame_1_balloon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(770)
        assert_that(match.top_left[1]).is_equal_to(300)
        assert_that(match.bottom_right[0]).is_equal_to(830)
        assert_that(match.bottom_right[1]).is_equal_to(362)

    def test_frame_1_balloon_sift(self):
        threshold = unit_constants.cherrystone_balloon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_balloon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(770, 830)
        assert_that(match.location[1]).is_between(300, 362)

    def test_frame_2_balloon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(434)
        assert_that(match.top_left[1]).is_equal_to(300)
        assert_that(match.bottom_right[0]).is_equal_to(494)
        assert_that(match.bottom_right[1]).is_equal_to(362)

    def test_frame_2_balloon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(434)
        assert_that(match.top_left[1]).is_equal_to(300)
        assert_that(match.bottom_right[0]).is_equal_to(494)
        assert_that(match.bottom_right[1]).is_equal_to(362)

    def test_frame_2_balloon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_balloon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_balloon',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(434)
        assert_that(match.top_left[1]).is_equal_to(300)
        assert_that(match.bottom_right[0]).is_equal_to(494)
        assert_that(match.bottom_right[1]).is_equal_to(362)

    def test_frame_2_balloon_sift(self):
        threshold = unit_constants.cherrystone_balloon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_balloon',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(434, 494)
        assert_that(match.location[1]).is_between(300, 362)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPY ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_harpy_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(876)
        assert_that(match.top_left[1]).is_equal_to(112)
        assert_that(match.bottom_right[0]).is_equal_to(938)
        assert_that(match.bottom_right[1]).is_equal_to(168)

    def test_frame_1_harpy_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(876)
        assert_that(match.top_left[1]).is_equal_to(112)
        assert_that(match.bottom_right[0]).is_equal_to(938)
        assert_that(match.bottom_right[1]).is_equal_to(168)

    def test_frame_1_harpy_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(876)
        assert_that(match.top_left[1]).is_equal_to(112)
        assert_that(match.bottom_right[0]).is_equal_to(938)
        assert_that(match.bottom_right[1]).is_equal_to(168)

    def test_frame_1_harpy_sift(self):
        threshold = unit_constants.cherrystone_harpy_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpy',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(876, 938)
        assert_that(match.location[1]).is_between(112, 168)

    def test_frame_2_harpy_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(346)
        assert_that(match.top_left[1]).is_equal_to(112)
        assert_that(match.bottom_right[0]).is_equal_to(408)
        assert_that(match.bottom_right[1]).is_equal_to(168)

    def test_frame_2_harpy_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(346)
        assert_that(match.top_left[1]).is_equal_to(112)
        assert_that(match.bottom_right[0]).is_equal_to(408)
        assert_that(match.bottom_right[1]).is_equal_to(168)

    def test_frame_2_harpy_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpy_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpy',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(346)
        assert_that(match.top_left[1]).is_equal_to(112)
        assert_that(match.bottom_right[0]).is_equal_to(408)
        assert_that(match.bottom_right[1]).is_equal_to(168)

    def test_frame_2_harpy_sift(self):
        threshold = unit_constants.cherrystone_harpy_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpy',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(346, 408)
        assert_that(match.location[1]).is_between(112, 168)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WITCH ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_witch_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(878)
        assert_that(match.top_left[1]).is_equal_to(214)
        assert_that(match.bottom_right[0]).is_equal_to(926)
        assert_that(match.bottom_right[1]).is_equal_to(264)

    def test_frame_1_witch_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(878)
        assert_that(match.top_left[1]).is_equal_to(214)
        assert_that(match.bottom_right[0]).is_equal_to(926)
        assert_that(match.bottom_right[1]).is_equal_to(264)

    def test_frame_1_witch_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(878)
        assert_that(match.top_left[1]).is_equal_to(214)
        assert_that(match.bottom_right[0]).is_equal_to(926)
        assert_that(match.bottom_right[1]).is_equal_to(264)

    def test_frame_1_witch_sift(self):
        threshold = unit_constants.cherrystone_witch_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_witch',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(878, 926)
        assert_that(match.location[1]).is_between(214, 264)

    def test_frame_2_witch_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(348)
        assert_that(match.top_left[1]).is_equal_to(214)
        assert_that(match.bottom_right[0]).is_equal_to(396)
        assert_that(match.bottom_right[1]).is_equal_to(264)

    def test_frame_2_witch_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(348)
        assert_that(match.top_left[1]).is_equal_to(214)
        assert_that(match.bottom_right[0]).is_equal_to(396)
        assert_that(match.bottom_right[1]).is_equal_to(264)

    def test_frame_2_witch_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_witch_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_witch',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(348)
        assert_that(match.top_left[1]).is_equal_to(214)
        assert_that(match.bottom_right[0]).is_equal_to(396)
        assert_that(match.bottom_right[1]).is_equal_to(264)

    def test_frame_2_witch_sift(self):
        threshold = unit_constants.cherrystone_witch_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_witch',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(348, 396)
        assert_that(match.location[1]).is_between(214, 264)

    # ----------------------------------------------------------------------------
    # ---------------------------------- DRAGON ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_dragon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(872)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(934)
        assert_that(match.bottom_right[1]).is_equal_to(354)

    def test_frame_1_dragon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(872)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(934)
        assert_that(match.bottom_right[1]).is_equal_to(354)

    def test_frame_1_dragon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(872)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(934)
        assert_that(match.bottom_right[1]).is_equal_to(354)

    def test_frame_1_dragon_sift(self):
        threshold = unit_constants.cherrystone_dragon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_emberwing',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(872, 934)
        assert_that(match.location[1]).is_between(320, 354)

    def test_frame_2_dragon_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(342)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(404)
        assert_that(match.bottom_right[1]).is_equal_to(354)

    def test_frame_2_dragon_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(342)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(404)
        assert_that(match.bottom_right[1]).is_equal_to(354)

    def test_frame_2_dragon_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_dragon_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_emberwing',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(342)
        assert_that(match.top_left[1]).is_equal_to(320)
        assert_that(match.bottom_right[0]).is_equal_to(404)
        assert_that(match.bottom_right[1]).is_equal_to(354)

    def test_frame_2_dragon_sift(self):
        threshold = unit_constants.cherrystone_dragon_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_emberwing',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(342, 404)
        assert_that(match.location[1]).is_between(320, 354)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_barge_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(450)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(502)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_frame_1_barge_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(450)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(502)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_frame_1_barge_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(450)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(502)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_frame_1_barge_sift(self):
        threshold = unit_constants.cherrystone_barge_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_barge',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(450, 502)
        assert_that(match.location[1]).is_between(520, 560)

    def test_frame_2_barge_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(786)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(838)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_frame_2_barge_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(786)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(838)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_frame_2_barge_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barge_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_barge',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(786)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(838)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_frame_2_barge_sift(self):
        threshold = unit_constants.cherrystone_barge_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_barge',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(786, 838)
        assert_that(match.location[1]).is_between(520, 560)

    # ----------------------------------------------------------------------------
    # ---------------------------------- SEA TURTLE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_seaturtle_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(544)
        assert_that(match.top_left[1]).is_equal_to(530)
        assert_that(match.bottom_right[0]).is_equal_to(596)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_frame_1_seaturtle_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(544)
        assert_that(match.top_left[1]).is_equal_to(530)
        assert_that(match.bottom_right[0]).is_equal_to(596)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_frame_1_seaturtle_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(544)
        assert_that(match.top_left[1]).is_equal_to(530)
        assert_that(match.bottom_right[0]).is_equal_to(596)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_frame_1_seaturtle_sift(self):
        threshold = unit_constants.cherrystone_seaturtle_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_sea_turtle',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(544, 596)
        assert_that(match.location[1]).is_between(530, 569)

    def test_frame_2_seaturtle_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(688)
        assert_that(match.top_left[1]).is_equal_to(530)
        assert_that(match.bottom_right[0]).is_equal_to(740)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_frame_2_seaturtle_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(688)
        assert_that(match.top_left[1]).is_equal_to(530)
        assert_that(match.bottom_right[0]).is_equal_to(740)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_frame_2_seaturtle_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_seaturtle_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_sea_turtle',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(688)
        assert_that(match.top_left[1]).is_equal_to(530)
        assert_that(match.bottom_right[0]).is_equal_to(740)
        assert_that(match.bottom_right[1]).is_equal_to(560)

    def test_frame_2_seaturtle_sift(self):
        threshold = unit_constants.cherrystone_seaturtle_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_sea_turtle',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(688, 740)
        assert_that(match.location[1]).is_between(530, 560)

    # ----------------------------------------------------------------------------
    # ---------------------------------- HARPOON SHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_harpoonship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(641)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(695)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_frame_1_harpoonship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(641)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(695)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_frame_1_harpoonship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(641)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(695)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_frame_1_harpoonship_sift(self):
        threshold = unit_constants.cherrystone_harpoonship_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpoon_ship',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(641, 695)
        assert_that(match.location[1]).is_between(516, 564)

    def test_frame_2_harpoonship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(593)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(647)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_frame_2_harpoonship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(593)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(647)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_frame_2_harpoonship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_harpoonship_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_harpoon_ship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(593)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(647)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_frame_2_harpoonship_sift(self):
        threshold = unit_constants.cherrystone_harpoonship_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_harpoon_ship',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(593, 647)
        assert_that(match.location[1]).is_between(516, 564)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WARSHIP ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_warship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(732)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(794)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_frame_1_warship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(732)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(794)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_frame_1_warship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(732)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(794)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_frame_1_warship_sift(self):
        threshold = unit_constants.cherrystone_warship_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_warship',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(732, 794)
        assert_that(match.location[1]).is_between(516, 564)

    def test_frame_2_warship_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(492)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(554)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_frame_2_warship_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(492)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(554)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_frame_2_warship_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_warship_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_warship',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(492)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(554)
        assert_that(match.bottom_right[1]).is_equal_to(564)

    def test_frame_2_warship_sift(self):
        threshold = unit_constants.cherrystone_warship_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_warship',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(492, 554)
        assert_that(match.location[1]).is_between(516, 564)

    # ----------------------------------------------------------------------------
    # ---------------------------------- MERFOLK ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_merfolk_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(840)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(886)
        assert_that(match.bottom_right[1]).is_equal_to(562)

    def test_frame_1_merfolk_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(840)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(886)
        assert_that(match.bottom_right[1]).is_equal_to(562)

    def test_frame_1_merfolk_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(840)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(886)
        assert_that(match.bottom_right[1]).is_equal_to(562)

    def test_frame_1_merfolk_sift(self):
        threshold = unit_constants.cherrystone_merfolk_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_merfolk',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(840, 886)
        assert_that(match.location[1]).is_between(520, 562)

    def test_frame_2_merfolk_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(408)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(454)
        assert_that(match.bottom_right[1]).is_equal_to(562)

    def test_frame_2_merfolk_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(408)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(454)
        assert_that(match.bottom_right[1]).is_equal_to(562)

    def test_frame_2_merfolk_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_merfolk_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_template_matching('cherrystone_merfolk',
                                                                threshold=threshold,
                                                                method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(408)
        assert_that(match.top_left[1]).is_equal_to(520)
        assert_that(match.bottom_right[0]).is_equal_to(454)
        assert_that(match.bottom_right[1]).is_equal_to(562)

    def test_frame_2_merfolk_sift(self):
        threshold = unit_constants.cherrystone_merfolk_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_unit_with_sift('cherrystone_merfolk',
                                                   threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(408, 454)
        assert_that(match.location[1]).is_between(520, 562)

    # ----------------------------------------------------------------------------
    # ---------------------------------- BARRACKS ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_barracks_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(546)
        assert_that(match.top_left[1]).is_equal_to(420)
        assert_that(match.bottom_right[0]).is_equal_to(596)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_frame_1_barracks_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(546)
        assert_that(match.top_left[1]).is_equal_to(420)
        assert_that(match.bottom_right[0]).is_equal_to(596)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_frame_1_barracks_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(546)
        assert_that(match.top_left[1]).is_equal_to(420)
        assert_that(match.bottom_right[0]).is_equal_to(596)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_frame_1_barracks_sift(self):
        threshold = unit_constants.cherrystone_barracks_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_barracks',
                                                        threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(546, 596)
        assert_that(match.location[1]).is_between(420, 480)

    def test_frame_2_barracks_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(642)
        assert_that(match.top_left[1]).is_equal_to(420)
        assert_that(match.bottom_right[0]).is_equal_to(692)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_frame_2_barracks_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(642)
        assert_that(match.top_left[1]).is_equal_to(420)
        assert_that(match.bottom_right[0]).is_equal_to(692)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_frame_2_barracks_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_barracks_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_barracks',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(642)
        assert_that(match.top_left[1]).is_equal_to(420)
        assert_that(match.bottom_right[0]).is_equal_to(692)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_frame_2_barracks_sift(self):
        threshold = unit_constants.cherrystone_barracks_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_barracks',
                                                        threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(642, 692)
        assert_that(match.location[1]).is_between(420, 480)

    # ----------------------------------------------------------------------------
    # ---------------------------------- PORT ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_port_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(972)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(1026)
        assert_that(match.bottom_right[1]).is_equal_to(578)

    def test_frame_1_port_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(972)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(1026)
        assert_that(match.bottom_right[1]).is_equal_to(578)

    def test_frame_1_port_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(972)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(1026)
        assert_that(match.bottom_right[1]).is_equal_to(578)

    def test_frame_1_port_sift(self):
        threshold = unit_constants.cherrystone_port_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_port',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(972, 1026)
        assert_that(match.location[1]).is_between(516, 578)

    def test_frame_2_port_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(299)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(353)
        assert_that(match.bottom_right[1]).is_equal_to(578)

    def test_frame_2_port_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(299)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(353)
        assert_that(match.bottom_right[1]).is_equal_to(578)

    def test_frame_2_port_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_port_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_port',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(299)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(353)
        assert_that(match.bottom_right[1]).is_equal_to(578)

    def test_frame_2_port_sift(self):
        threshold = unit_constants.cherrystone_port_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_port',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(299, 353)
        assert_that(match.location[1]).is_between(516, 578)

    # ----------------------------------------------------------------------------
    # ---------------------------------- STRONGHOLD ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_stronghold_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(402)
        assert_that(match.bottom_right[0]).is_equal_to(496)
        assert_that(match.bottom_right[1]).is_equal_to(482)

    def test_frame_1_stronghold_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(402)
        assert_that(match.bottom_right[0]).is_equal_to(496)
        assert_that(match.bottom_right[1]).is_equal_to(482)

    def test_frame_1_stronghold_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(446)
        assert_that(match.top_left[1]).is_equal_to(402)
        assert_that(match.bottom_right[0]).is_equal_to(496)
        assert_that(match.bottom_right[1]).is_equal_to(482)

    def test_frame_1_stronghold_sift(self):
        threshold = unit_constants.cherrystone_stronghold_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_stronghold',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(446, 496)
        assert_that(match.location[1]).is_between(402, 482)

    def test_frame_2_stronghold_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(736)
        assert_that(match.top_left[1]).is_equal_to(402)
        assert_that(match.bottom_right[0]).is_equal_to(786)
        assert_that(match.bottom_right[1]).is_equal_to(482)

    def test_frame_2_stronghold_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(736)
        assert_that(match.top_left[1]).is_equal_to(402)
        assert_that(match.bottom_right[0]).is_equal_to(786)
        assert_that(match.bottom_right[1]).is_equal_to(482)

    def test_frame_2_stronghold_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_stronghold_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_stronghold',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(736)
        assert_that(match.top_left[1]).is_equal_to(402)
        assert_that(match.bottom_right[0]).is_equal_to(786)
        assert_that(match.bottom_right[1]).is_equal_to(482)

    def test_frame_2_stronghold_sift(self):
        threshold = unit_constants.cherrystone_stronghold_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_stronghold',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(736, 786)
        assert_that(match.location[1]).is_between(402, 482)

    # ----------------------------------------------------------------------------
    # ---------------------------------- TOWER ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_tower_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(738)
        assert_that(match.top_left[1]).is_equal_to(416)
        assert_that(match.bottom_right[0]).is_equal_to(784)
        assert_that(match.bottom_right[1]).is_equal_to(476)

    def test_frame_1_tower_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(738)
        assert_that(match.top_left[1]).is_equal_to(416)
        assert_that(match.bottom_right[0]).is_equal_to(784)
        assert_that(match.bottom_right[1]).is_equal_to(476)

    def test_frame_1_tower_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(738)
        assert_that(match.top_left[1]).is_equal_to(416)
        assert_that(match.bottom_right[0]).is_equal_to(784)
        assert_that(match.bottom_right[1]).is_equal_to(476)

    def test_frame_1_tower_sift(self):
        threshold = unit_constants.cherrystone_tower_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_tower',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(738, 784)
        assert_that(match.location[1]).is_between(416, 476)

    def test_frame_2_tower_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(450)
        assert_that(match.top_left[1]).is_equal_to(416)
        assert_that(match.bottom_right[0]).is_equal_to(496)
        assert_that(match.bottom_right[1]).is_equal_to(476)

    def test_frame_2_tower_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(450)
        assert_that(match.top_left[1]).is_equal_to(416)
        assert_that(match.bottom_right[0]).is_equal_to(496)
        assert_that(match.bottom_right[1]).is_equal_to(476)

    def test_frame_2_tower_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_tower_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_tower',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(450)
        assert_that(match.top_left[1]).is_equal_to(416)
        assert_that(match.bottom_right[0]).is_equal_to(496)
        assert_that(match.bottom_right[1]).is_equal_to(476)

    def test_frame_2_tower_sift(self):
        threshold = unit_constants.cherrystone_tower_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_tower',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(450, 496)
        assert_that(match.location[1]).is_between(416, 476)

    # ----------------------------------------------------------------------------
    # ---------------------------------- VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_village_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(638)
        assert_that(match.top_left[1]).is_equal_to(424)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_frame_1_village_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(638)
        assert_that(match.top_left[1]).is_equal_to(424)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_frame_1_village_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(638)
        assert_that(match.top_left[1]).is_equal_to(424)
        assert_that(match.bottom_right[0]).is_equal_to(690)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_frame_1_village_sift(self):
        threshold = unit_constants.cherrystone_village_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_village',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(638, 690)
        assert_that(match.location[1]).is_between(424, 480)

    def test_frame_2_village_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(542)
        assert_that(match.top_left[1]).is_equal_to(424)
        assert_that(match.bottom_right[0]).is_equal_to(594)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_frame_2_village_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(542)
        assert_that(match.top_left[1]).is_equal_to(424)
        assert_that(match.bottom_right[0]).is_equal_to(594)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_frame_2_village_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_village_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_village',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(542)
        assert_that(match.top_left[1]).is_equal_to(424)
        assert_that(match.bottom_right[0]).is_equal_to(594)
        assert_that(match.bottom_right[1]).is_equal_to(480)

    def test_frame_2_village_sift(self):
        threshold = unit_constants.cherrystone_village_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_village',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(542, 594)
        assert_that(match.location[1]).is_between(424, 480)

    # ----------------------------------------------------------------------------
    # ---------------------------------- WATER VILLAGE ----------------------------------
    # ----------------------------------------------------------------------------

    def test_frame_1_watervillage_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(302)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(352)
        assert_that(match.bottom_right[1]).is_equal_to(574)

    def test_frame_1_watervillage_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(302)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(352)
        assert_that(match.bottom_right[1]).is_equal_to(574)

    def test_frame_1_watervillage_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(302)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(352)
        assert_that(match.bottom_right[1]).is_equal_to(574)

    def test_frame_1_watervillage_sift(self):
        threshold = unit_constants.cherrystone_watervillage_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_1.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_watervillage',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(302, 354)
        assert_that(match.location[1]).is_between(516, 574)

    def test_frame_2_watervillage_standard_template_matching_cross_corr(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(974)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(1024)
        assert_that(match.bottom_right[1]).is_equal_to(574)

    def test_frame_2_watervillage_standard_template_matching_corr_coeff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_corr_coeff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.CORRELATION_COEFFICIENT_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(974)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(1024)
        assert_that(match.bottom_right[1]).is_equal_to(574)

    def test_frame_2_watervillage_standard_template_matching_square_diff(self):
        threshold = unit_constants.cherrystone_watervillage_standard_template_matching_square_diff_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_template_matching('cherrystone_watervillage',
                                                                    threshold=threshold,
                                                                    method=cmp504.computer_vision.TemplateMatchingMethod.SQUARE_DIFFERENCE_NORMALIZED)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.top_left[0]).is_equal_to(974)
        assert_that(match.top_left[1]).is_equal_to(516)
        assert_that(match.bottom_right[0]).is_equal_to(1024)
        assert_that(match.bottom_right[1]).is_equal_to(574)

    def test_frame_2_watervillage_sift(self):
        threshold = unit_constants.cherrystone_watervillage_sift_threshold
        wargroove_ctrl.vision.load_frame(self.__get_eval_folder() + '1280x720_movement_config_2.png')
        match = wargroove_ctrl.find_building_with_sift('cherrystone_watervillage',
                                                       threshold=threshold)

        wargroove_ctrl.log_match_for_evaluation(self.id(), match, threshold)

        assert_that(match).is_not_none()
        assert_that(match.location[0]).is_between(974, 1024)
        assert_that(match.location[1]).is_between(516, 574)
