# /* **************************************************************************
#  *                                                                          *
#  *     (C) Copyright Paul Mensonides 2002.
#  *     Distributed under the Boost Software License, Version 1.0. (See
#  *     accompanying file LICENSE_1_0.txt or copy at
#  *     http://www.boost.org/LICENSE_1_0.txt)
#  *                                                                          *
#  ************************************************************************** */
#
# /* See http://www.boost.org for most recent version. */
#
# ifndef MSGPACK_PREPROCESSOR_SEQ_FOLD_RIGHT_HPP
# define MSGPACK_PREPROCESSOR_SEQ_FOLD_RIGHT_HPP
#
# include <msgpack/preprocessor/cat.hpp>
# include <msgpack/preprocessor/detail/auto_rec.hpp>
# include <msgpack/preprocessor/seq/fold_left.hpp>
# include <msgpack/preprocessor/seq/reverse.hpp>
# include <msgpack/preprocessor/seq/seq.hpp>
#
# /* MSGPACK_PP_SEQ_FOLD_RIGHT */
#
# if 0
#    define MSGPACK_PP_SEQ_FOLD_RIGHT(op, state, seq) ...
# endif
#
# define MSGPACK_PP_SEQ_FOLD_RIGHT MSGPACK_PP_CAT(MSGPACK_PP_SEQ_FOLD_RIGHT_, MSGPACK_PP_AUTO_REC(MSGPACK_PP_SEQ_FOLD_LEFT_P, 256))
#
# define MSGPACK_PP_SEQ_FOLD_RIGHT_257(op, st, ss) MSGPACK_PP_ERROR(0x0005)
#
# define MSGPACK_PP_SEQ_FOLD_RIGHT_1(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_1(op, st, MSGPACK_PP_SEQ_REVERSE_S(2, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_2(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_2(op, st, MSGPACK_PP_SEQ_REVERSE_S(3, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_3(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_3(op, st, MSGPACK_PP_SEQ_REVERSE_S(4, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_4(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_4(op, st, MSGPACK_PP_SEQ_REVERSE_S(5, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_5(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_5(op, st, MSGPACK_PP_SEQ_REVERSE_S(6, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_6(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_6(op, st, MSGPACK_PP_SEQ_REVERSE_S(7, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_7(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_7(op, st, MSGPACK_PP_SEQ_REVERSE_S(8, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_8(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_8(op, st, MSGPACK_PP_SEQ_REVERSE_S(9, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_9(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_9(op, st, MSGPACK_PP_SEQ_REVERSE_S(10, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_10(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_10(op, st, MSGPACK_PP_SEQ_REVERSE_S(11, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_11(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_11(op, st, MSGPACK_PP_SEQ_REVERSE_S(12, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_12(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_12(op, st, MSGPACK_PP_SEQ_REVERSE_S(13, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_13(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_13(op, st, MSGPACK_PP_SEQ_REVERSE_S(14, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_14(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_14(op, st, MSGPACK_PP_SEQ_REVERSE_S(15, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_15(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_15(op, st, MSGPACK_PP_SEQ_REVERSE_S(16, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_16(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_16(op, st, MSGPACK_PP_SEQ_REVERSE_S(17, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_17(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_17(op, st, MSGPACK_PP_SEQ_REVERSE_S(18, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_18(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_18(op, st, MSGPACK_PP_SEQ_REVERSE_S(19, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_19(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_19(op, st, MSGPACK_PP_SEQ_REVERSE_S(20, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_20(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_20(op, st, MSGPACK_PP_SEQ_REVERSE_S(21, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_21(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_21(op, st, MSGPACK_PP_SEQ_REVERSE_S(22, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_22(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_22(op, st, MSGPACK_PP_SEQ_REVERSE_S(23, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_23(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_23(op, st, MSGPACK_PP_SEQ_REVERSE_S(24, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_24(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_24(op, st, MSGPACK_PP_SEQ_REVERSE_S(25, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_25(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_25(op, st, MSGPACK_PP_SEQ_REVERSE_S(26, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_26(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_26(op, st, MSGPACK_PP_SEQ_REVERSE_S(27, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_27(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_27(op, st, MSGPACK_PP_SEQ_REVERSE_S(28, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_28(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_28(op, st, MSGPACK_PP_SEQ_REVERSE_S(29, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_29(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_29(op, st, MSGPACK_PP_SEQ_REVERSE_S(30, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_30(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_30(op, st, MSGPACK_PP_SEQ_REVERSE_S(31, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_31(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_31(op, st, MSGPACK_PP_SEQ_REVERSE_S(32, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_32(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_32(op, st, MSGPACK_PP_SEQ_REVERSE_S(33, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_33(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_33(op, st, MSGPACK_PP_SEQ_REVERSE_S(34, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_34(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_34(op, st, MSGPACK_PP_SEQ_REVERSE_S(35, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_35(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_35(op, st, MSGPACK_PP_SEQ_REVERSE_S(36, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_36(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_36(op, st, MSGPACK_PP_SEQ_REVERSE_S(37, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_37(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_37(op, st, MSGPACK_PP_SEQ_REVERSE_S(38, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_38(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_38(op, st, MSGPACK_PP_SEQ_REVERSE_S(39, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_39(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_39(op, st, MSGPACK_PP_SEQ_REVERSE_S(40, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_40(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_40(op, st, MSGPACK_PP_SEQ_REVERSE_S(41, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_41(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_41(op, st, MSGPACK_PP_SEQ_REVERSE_S(42, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_42(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_42(op, st, MSGPACK_PP_SEQ_REVERSE_S(43, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_43(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_43(op, st, MSGPACK_PP_SEQ_REVERSE_S(44, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_44(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_44(op, st, MSGPACK_PP_SEQ_REVERSE_S(45, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_45(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_45(op, st, MSGPACK_PP_SEQ_REVERSE_S(46, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_46(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_46(op, st, MSGPACK_PP_SEQ_REVERSE_S(47, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_47(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_47(op, st, MSGPACK_PP_SEQ_REVERSE_S(48, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_48(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_48(op, st, MSGPACK_PP_SEQ_REVERSE_S(49, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_49(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_49(op, st, MSGPACK_PP_SEQ_REVERSE_S(50, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_50(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_50(op, st, MSGPACK_PP_SEQ_REVERSE_S(51, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_51(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_51(op, st, MSGPACK_PP_SEQ_REVERSE_S(52, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_52(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_52(op, st, MSGPACK_PP_SEQ_REVERSE_S(53, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_53(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_53(op, st, MSGPACK_PP_SEQ_REVERSE_S(54, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_54(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_54(op, st, MSGPACK_PP_SEQ_REVERSE_S(55, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_55(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_55(op, st, MSGPACK_PP_SEQ_REVERSE_S(56, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_56(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_56(op, st, MSGPACK_PP_SEQ_REVERSE_S(57, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_57(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_57(op, st, MSGPACK_PP_SEQ_REVERSE_S(58, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_58(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_58(op, st, MSGPACK_PP_SEQ_REVERSE_S(59, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_59(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_59(op, st, MSGPACK_PP_SEQ_REVERSE_S(60, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_60(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_60(op, st, MSGPACK_PP_SEQ_REVERSE_S(61, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_61(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_61(op, st, MSGPACK_PP_SEQ_REVERSE_S(62, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_62(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_62(op, st, MSGPACK_PP_SEQ_REVERSE_S(63, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_63(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_63(op, st, MSGPACK_PP_SEQ_REVERSE_S(64, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_64(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_64(op, st, MSGPACK_PP_SEQ_REVERSE_S(65, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_65(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_65(op, st, MSGPACK_PP_SEQ_REVERSE_S(66, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_66(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_66(op, st, MSGPACK_PP_SEQ_REVERSE_S(67, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_67(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_67(op, st, MSGPACK_PP_SEQ_REVERSE_S(68, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_68(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_68(op, st, MSGPACK_PP_SEQ_REVERSE_S(69, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_69(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_69(op, st, MSGPACK_PP_SEQ_REVERSE_S(70, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_70(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_70(op, st, MSGPACK_PP_SEQ_REVERSE_S(71, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_71(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_71(op, st, MSGPACK_PP_SEQ_REVERSE_S(72, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_72(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_72(op, st, MSGPACK_PP_SEQ_REVERSE_S(73, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_73(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_73(op, st, MSGPACK_PP_SEQ_REVERSE_S(74, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_74(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_74(op, st, MSGPACK_PP_SEQ_REVERSE_S(75, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_75(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_75(op, st, MSGPACK_PP_SEQ_REVERSE_S(76, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_76(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_76(op, st, MSGPACK_PP_SEQ_REVERSE_S(77, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_77(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_77(op, st, MSGPACK_PP_SEQ_REVERSE_S(78, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_78(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_78(op, st, MSGPACK_PP_SEQ_REVERSE_S(79, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_79(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_79(op, st, MSGPACK_PP_SEQ_REVERSE_S(80, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_80(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_80(op, st, MSGPACK_PP_SEQ_REVERSE_S(81, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_81(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_81(op, st, MSGPACK_PP_SEQ_REVERSE_S(82, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_82(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_82(op, st, MSGPACK_PP_SEQ_REVERSE_S(83, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_83(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_83(op, st, MSGPACK_PP_SEQ_REVERSE_S(84, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_84(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_84(op, st, MSGPACK_PP_SEQ_REVERSE_S(85, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_85(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_85(op, st, MSGPACK_PP_SEQ_REVERSE_S(86, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_86(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_86(op, st, MSGPACK_PP_SEQ_REVERSE_S(87, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_87(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_87(op, st, MSGPACK_PP_SEQ_REVERSE_S(88, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_88(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_88(op, st, MSGPACK_PP_SEQ_REVERSE_S(89, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_89(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_89(op, st, MSGPACK_PP_SEQ_REVERSE_S(90, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_90(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_90(op, st, MSGPACK_PP_SEQ_REVERSE_S(91, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_91(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_91(op, st, MSGPACK_PP_SEQ_REVERSE_S(92, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_92(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_92(op, st, MSGPACK_PP_SEQ_REVERSE_S(93, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_93(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_93(op, st, MSGPACK_PP_SEQ_REVERSE_S(94, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_94(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_94(op, st, MSGPACK_PP_SEQ_REVERSE_S(95, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_95(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_95(op, st, MSGPACK_PP_SEQ_REVERSE_S(96, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_96(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_96(op, st, MSGPACK_PP_SEQ_REVERSE_S(97, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_97(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_97(op, st, MSGPACK_PP_SEQ_REVERSE_S(98, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_98(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_98(op, st, MSGPACK_PP_SEQ_REVERSE_S(99, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_99(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_99(op, st, MSGPACK_PP_SEQ_REVERSE_S(100, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_100(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_100(op, st, MSGPACK_PP_SEQ_REVERSE_S(101, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_101(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_101(op, st, MSGPACK_PP_SEQ_REVERSE_S(102, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_102(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_102(op, st, MSGPACK_PP_SEQ_REVERSE_S(103, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_103(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_103(op, st, MSGPACK_PP_SEQ_REVERSE_S(104, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_104(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_104(op, st, MSGPACK_PP_SEQ_REVERSE_S(105, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_105(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_105(op, st, MSGPACK_PP_SEQ_REVERSE_S(106, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_106(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_106(op, st, MSGPACK_PP_SEQ_REVERSE_S(107, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_107(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_107(op, st, MSGPACK_PP_SEQ_REVERSE_S(108, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_108(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_108(op, st, MSGPACK_PP_SEQ_REVERSE_S(109, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_109(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_109(op, st, MSGPACK_PP_SEQ_REVERSE_S(110, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_110(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_110(op, st, MSGPACK_PP_SEQ_REVERSE_S(111, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_111(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_111(op, st, MSGPACK_PP_SEQ_REVERSE_S(112, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_112(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_112(op, st, MSGPACK_PP_SEQ_REVERSE_S(113, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_113(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_113(op, st, MSGPACK_PP_SEQ_REVERSE_S(114, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_114(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_114(op, st, MSGPACK_PP_SEQ_REVERSE_S(115, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_115(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_115(op, st, MSGPACK_PP_SEQ_REVERSE_S(116, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_116(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_116(op, st, MSGPACK_PP_SEQ_REVERSE_S(117, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_117(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_117(op, st, MSGPACK_PP_SEQ_REVERSE_S(118, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_118(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_118(op, st, MSGPACK_PP_SEQ_REVERSE_S(119, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_119(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_119(op, st, MSGPACK_PP_SEQ_REVERSE_S(120, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_120(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_120(op, st, MSGPACK_PP_SEQ_REVERSE_S(121, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_121(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_121(op, st, MSGPACK_PP_SEQ_REVERSE_S(122, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_122(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_122(op, st, MSGPACK_PP_SEQ_REVERSE_S(123, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_123(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_123(op, st, MSGPACK_PP_SEQ_REVERSE_S(124, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_124(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_124(op, st, MSGPACK_PP_SEQ_REVERSE_S(125, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_125(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_125(op, st, MSGPACK_PP_SEQ_REVERSE_S(126, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_126(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_126(op, st, MSGPACK_PP_SEQ_REVERSE_S(127, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_127(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_127(op, st, MSGPACK_PP_SEQ_REVERSE_S(128, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_128(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_128(op, st, MSGPACK_PP_SEQ_REVERSE_S(129, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_129(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_129(op, st, MSGPACK_PP_SEQ_REVERSE_S(130, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_130(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_130(op, st, MSGPACK_PP_SEQ_REVERSE_S(131, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_131(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_131(op, st, MSGPACK_PP_SEQ_REVERSE_S(132, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_132(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_132(op, st, MSGPACK_PP_SEQ_REVERSE_S(133, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_133(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_133(op, st, MSGPACK_PP_SEQ_REVERSE_S(134, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_134(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_134(op, st, MSGPACK_PP_SEQ_REVERSE_S(135, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_135(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_135(op, st, MSGPACK_PP_SEQ_REVERSE_S(136, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_136(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_136(op, st, MSGPACK_PP_SEQ_REVERSE_S(137, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_137(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_137(op, st, MSGPACK_PP_SEQ_REVERSE_S(138, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_138(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_138(op, st, MSGPACK_PP_SEQ_REVERSE_S(139, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_139(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_139(op, st, MSGPACK_PP_SEQ_REVERSE_S(140, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_140(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_140(op, st, MSGPACK_PP_SEQ_REVERSE_S(141, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_141(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_141(op, st, MSGPACK_PP_SEQ_REVERSE_S(142, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_142(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_142(op, st, MSGPACK_PP_SEQ_REVERSE_S(143, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_143(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_143(op, st, MSGPACK_PP_SEQ_REVERSE_S(144, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_144(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_144(op, st, MSGPACK_PP_SEQ_REVERSE_S(145, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_145(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_145(op, st, MSGPACK_PP_SEQ_REVERSE_S(146, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_146(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_146(op, st, MSGPACK_PP_SEQ_REVERSE_S(147, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_147(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_147(op, st, MSGPACK_PP_SEQ_REVERSE_S(148, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_148(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_148(op, st, MSGPACK_PP_SEQ_REVERSE_S(149, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_149(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_149(op, st, MSGPACK_PP_SEQ_REVERSE_S(150, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_150(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_150(op, st, MSGPACK_PP_SEQ_REVERSE_S(151, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_151(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_151(op, st, MSGPACK_PP_SEQ_REVERSE_S(152, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_152(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_152(op, st, MSGPACK_PP_SEQ_REVERSE_S(153, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_153(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_153(op, st, MSGPACK_PP_SEQ_REVERSE_S(154, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_154(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_154(op, st, MSGPACK_PP_SEQ_REVERSE_S(155, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_155(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_155(op, st, MSGPACK_PP_SEQ_REVERSE_S(156, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_156(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_156(op, st, MSGPACK_PP_SEQ_REVERSE_S(157, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_157(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_157(op, st, MSGPACK_PP_SEQ_REVERSE_S(158, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_158(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_158(op, st, MSGPACK_PP_SEQ_REVERSE_S(159, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_159(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_159(op, st, MSGPACK_PP_SEQ_REVERSE_S(160, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_160(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_160(op, st, MSGPACK_PP_SEQ_REVERSE_S(161, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_161(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_161(op, st, MSGPACK_PP_SEQ_REVERSE_S(162, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_162(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_162(op, st, MSGPACK_PP_SEQ_REVERSE_S(163, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_163(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_163(op, st, MSGPACK_PP_SEQ_REVERSE_S(164, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_164(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_164(op, st, MSGPACK_PP_SEQ_REVERSE_S(165, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_165(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_165(op, st, MSGPACK_PP_SEQ_REVERSE_S(166, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_166(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_166(op, st, MSGPACK_PP_SEQ_REVERSE_S(167, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_167(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_167(op, st, MSGPACK_PP_SEQ_REVERSE_S(168, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_168(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_168(op, st, MSGPACK_PP_SEQ_REVERSE_S(169, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_169(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_169(op, st, MSGPACK_PP_SEQ_REVERSE_S(170, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_170(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_170(op, st, MSGPACK_PP_SEQ_REVERSE_S(171, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_171(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_171(op, st, MSGPACK_PP_SEQ_REVERSE_S(172, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_172(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_172(op, st, MSGPACK_PP_SEQ_REVERSE_S(173, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_173(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_173(op, st, MSGPACK_PP_SEQ_REVERSE_S(174, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_174(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_174(op, st, MSGPACK_PP_SEQ_REVERSE_S(175, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_175(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_175(op, st, MSGPACK_PP_SEQ_REVERSE_S(176, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_176(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_176(op, st, MSGPACK_PP_SEQ_REVERSE_S(177, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_177(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_177(op, st, MSGPACK_PP_SEQ_REVERSE_S(178, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_178(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_178(op, st, MSGPACK_PP_SEQ_REVERSE_S(179, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_179(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_179(op, st, MSGPACK_PP_SEQ_REVERSE_S(180, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_180(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_180(op, st, MSGPACK_PP_SEQ_REVERSE_S(181, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_181(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_181(op, st, MSGPACK_PP_SEQ_REVERSE_S(182, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_182(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_182(op, st, MSGPACK_PP_SEQ_REVERSE_S(183, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_183(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_183(op, st, MSGPACK_PP_SEQ_REVERSE_S(184, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_184(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_184(op, st, MSGPACK_PP_SEQ_REVERSE_S(185, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_185(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_185(op, st, MSGPACK_PP_SEQ_REVERSE_S(186, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_186(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_186(op, st, MSGPACK_PP_SEQ_REVERSE_S(187, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_187(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_187(op, st, MSGPACK_PP_SEQ_REVERSE_S(188, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_188(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_188(op, st, MSGPACK_PP_SEQ_REVERSE_S(189, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_189(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_189(op, st, MSGPACK_PP_SEQ_REVERSE_S(190, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_190(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_190(op, st, MSGPACK_PP_SEQ_REVERSE_S(191, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_191(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_191(op, st, MSGPACK_PP_SEQ_REVERSE_S(192, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_192(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_192(op, st, MSGPACK_PP_SEQ_REVERSE_S(193, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_193(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_193(op, st, MSGPACK_PP_SEQ_REVERSE_S(194, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_194(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_194(op, st, MSGPACK_PP_SEQ_REVERSE_S(195, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_195(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_195(op, st, MSGPACK_PP_SEQ_REVERSE_S(196, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_196(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_196(op, st, MSGPACK_PP_SEQ_REVERSE_S(197, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_197(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_197(op, st, MSGPACK_PP_SEQ_REVERSE_S(198, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_198(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_198(op, st, MSGPACK_PP_SEQ_REVERSE_S(199, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_199(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_199(op, st, MSGPACK_PP_SEQ_REVERSE_S(200, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_200(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_200(op, st, MSGPACK_PP_SEQ_REVERSE_S(201, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_201(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_201(op, st, MSGPACK_PP_SEQ_REVERSE_S(202, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_202(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_202(op, st, MSGPACK_PP_SEQ_REVERSE_S(203, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_203(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_203(op, st, MSGPACK_PP_SEQ_REVERSE_S(204, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_204(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_204(op, st, MSGPACK_PP_SEQ_REVERSE_S(205, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_205(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_205(op, st, MSGPACK_PP_SEQ_REVERSE_S(206, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_206(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_206(op, st, MSGPACK_PP_SEQ_REVERSE_S(207, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_207(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_207(op, st, MSGPACK_PP_SEQ_REVERSE_S(208, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_208(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_208(op, st, MSGPACK_PP_SEQ_REVERSE_S(209, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_209(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_209(op, st, MSGPACK_PP_SEQ_REVERSE_S(210, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_210(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_210(op, st, MSGPACK_PP_SEQ_REVERSE_S(211, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_211(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_211(op, st, MSGPACK_PP_SEQ_REVERSE_S(212, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_212(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_212(op, st, MSGPACK_PP_SEQ_REVERSE_S(213, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_213(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_213(op, st, MSGPACK_PP_SEQ_REVERSE_S(214, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_214(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_214(op, st, MSGPACK_PP_SEQ_REVERSE_S(215, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_215(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_215(op, st, MSGPACK_PP_SEQ_REVERSE_S(216, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_216(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_216(op, st, MSGPACK_PP_SEQ_REVERSE_S(217, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_217(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_217(op, st, MSGPACK_PP_SEQ_REVERSE_S(218, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_218(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_218(op, st, MSGPACK_PP_SEQ_REVERSE_S(219, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_219(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_219(op, st, MSGPACK_PP_SEQ_REVERSE_S(220, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_220(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_220(op, st, MSGPACK_PP_SEQ_REVERSE_S(221, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_221(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_221(op, st, MSGPACK_PP_SEQ_REVERSE_S(222, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_222(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_222(op, st, MSGPACK_PP_SEQ_REVERSE_S(223, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_223(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_223(op, st, MSGPACK_PP_SEQ_REVERSE_S(224, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_224(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_224(op, st, MSGPACK_PP_SEQ_REVERSE_S(225, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_225(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_225(op, st, MSGPACK_PP_SEQ_REVERSE_S(226, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_226(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_226(op, st, MSGPACK_PP_SEQ_REVERSE_S(227, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_227(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_227(op, st, MSGPACK_PP_SEQ_REVERSE_S(228, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_228(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_228(op, st, MSGPACK_PP_SEQ_REVERSE_S(229, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_229(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_229(op, st, MSGPACK_PP_SEQ_REVERSE_S(230, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_230(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_230(op, st, MSGPACK_PP_SEQ_REVERSE_S(231, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_231(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_231(op, st, MSGPACK_PP_SEQ_REVERSE_S(232, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_232(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_232(op, st, MSGPACK_PP_SEQ_REVERSE_S(233, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_233(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_233(op, st, MSGPACK_PP_SEQ_REVERSE_S(234, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_234(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_234(op, st, MSGPACK_PP_SEQ_REVERSE_S(235, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_235(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_235(op, st, MSGPACK_PP_SEQ_REVERSE_S(236, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_236(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_236(op, st, MSGPACK_PP_SEQ_REVERSE_S(237, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_237(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_237(op, st, MSGPACK_PP_SEQ_REVERSE_S(238, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_238(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_238(op, st, MSGPACK_PP_SEQ_REVERSE_S(239, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_239(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_239(op, st, MSGPACK_PP_SEQ_REVERSE_S(240, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_240(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_240(op, st, MSGPACK_PP_SEQ_REVERSE_S(241, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_241(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_241(op, st, MSGPACK_PP_SEQ_REVERSE_S(242, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_242(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_242(op, st, MSGPACK_PP_SEQ_REVERSE_S(243, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_243(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_243(op, st, MSGPACK_PP_SEQ_REVERSE_S(244, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_244(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_244(op, st, MSGPACK_PP_SEQ_REVERSE_S(245, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_245(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_245(op, st, MSGPACK_PP_SEQ_REVERSE_S(246, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_246(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_246(op, st, MSGPACK_PP_SEQ_REVERSE_S(247, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_247(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_247(op, st, MSGPACK_PP_SEQ_REVERSE_S(248, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_248(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_248(op, st, MSGPACK_PP_SEQ_REVERSE_S(249, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_249(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_249(op, st, MSGPACK_PP_SEQ_REVERSE_S(250, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_250(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_250(op, st, MSGPACK_PP_SEQ_REVERSE_S(251, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_251(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_251(op, st, MSGPACK_PP_SEQ_REVERSE_S(252, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_252(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_252(op, st, MSGPACK_PP_SEQ_REVERSE_S(253, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_253(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_253(op, st, MSGPACK_PP_SEQ_REVERSE_S(254, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_254(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_254(op, st, MSGPACK_PP_SEQ_REVERSE_S(255, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_255(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_255(op, st, MSGPACK_PP_SEQ_REVERSE_S(256, ss), MSGPACK_PP_SEQ_SIZE(ss))
# define MSGPACK_PP_SEQ_FOLD_RIGHT_256(op, st, ss) MSGPACK_PP_SEQ_FOLD_LEFT_I_256(op, st, MSGPACK_PP_SEQ_REVERSE_S(257, ss), MSGPACK_PP_SEQ_SIZE(ss))
#
# endif
