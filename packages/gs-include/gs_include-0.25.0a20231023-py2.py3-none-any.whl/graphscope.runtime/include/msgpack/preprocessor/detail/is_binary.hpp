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
# ifndef MSGPACK_PREPROCESSOR_DETAIL_IS_BINARY_HPP
# define MSGPACK_PREPROCESSOR_DETAIL_IS_BINARY_HPP
#
# include <msgpack/preprocessor/config/config.hpp>
# include <msgpack/preprocessor/detail/check.hpp>
#
# /* MSGPACK_PP_IS_BINARY */
#
# if ~MSGPACK_PP_CONFIG_FLAGS() & MSGPACK_PP_CONFIG_EDG()
#    define MSGPACK_PP_IS_BINARY(x) MSGPACK_PP_CHECK(x, MSGPACK_PP_IS_BINARY_CHECK)
# else
#    define MSGPACK_PP_IS_BINARY(x) MSGPACK_PP_IS_BINARY_I(x)
#    define MSGPACK_PP_IS_BINARY_I(x) MSGPACK_PP_CHECK(x, MSGPACK_PP_IS_BINARY_CHECK)
# endif
#
# define MSGPACK_PP_IS_BINARY_CHECK(a, b) 1
# define MSGPACK_PP_CHECK_RESULT_MSGPACK_PP_IS_BINARY_CHECK 0, MSGPACK_PP_NIL
#
# endif
