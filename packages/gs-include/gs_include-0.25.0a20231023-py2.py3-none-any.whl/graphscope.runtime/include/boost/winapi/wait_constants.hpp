/*
 * Copyright 2020 Andrey Semashev
 *
 * Distributed under the Boost Software License, Version 1.0.
 * See http://www.boost.org/LICENSE_1_0.txt
 */

#ifndef BOOST_WINAPI_WAIT_CONSTANTS_HPP_INCLUDED_
#define BOOST_WINAPI_WAIT_CONSTANTS_HPP_INCLUDED_

#include <boost/winapi/basic_types.hpp>
#include <boost/winapi/detail/header.hpp>

#ifdef BOOST_HAS_PRAGMA_ONCE
#pragma once
#endif

namespace boost {
namespace winapi {

#if defined( BOOST_USE_WINDOWS_H )

BOOST_CONSTEXPR_OR_CONST DWORD_ INFINITE_ = INFINITE;
BOOST_CONSTEXPR_OR_CONST DWORD_ WAIT_ABANDONED_ = WAIT_ABANDONED;
BOOST_CONSTEXPR_OR_CONST DWORD_ WAIT_OBJECT_0_ = WAIT_OBJECT_0;
BOOST_CONSTEXPR_OR_CONST DWORD_ WAIT_TIMEOUT_ = WAIT_TIMEOUT;
BOOST_CONSTEXPR_OR_CONST DWORD_ WAIT_FAILED_ = WAIT_FAILED;

#else // defined( BOOST_USE_WINDOWS_H )

BOOST_CONSTEXPR_OR_CONST DWORD_ INFINITE_ = (DWORD_)0xFFFFFFFF;
BOOST_CONSTEXPR_OR_CONST DWORD_ WAIT_ABANDONED_ = 0x00000080L;
BOOST_CONSTEXPR_OR_CONST DWORD_ WAIT_OBJECT_0_ = 0x00000000L;
BOOST_CONSTEXPR_OR_CONST DWORD_ WAIT_TIMEOUT_ = 0x00000102L;
BOOST_CONSTEXPR_OR_CONST DWORD_ WAIT_FAILED_ = (DWORD_)0xFFFFFFFF;

#endif // defined( BOOST_USE_WINDOWS_H )

BOOST_CONSTEXPR_OR_CONST DWORD_ infinite = INFINITE_;
BOOST_CONSTEXPR_OR_CONST DWORD_ wait_abandoned = WAIT_ABANDONED_;
BOOST_CONSTEXPR_OR_CONST DWORD_ wait_object_0 = WAIT_OBJECT_0_;
BOOST_CONSTEXPR_OR_CONST DWORD_ wait_timeout = WAIT_TIMEOUT_;
BOOST_CONSTEXPR_OR_CONST DWORD_ wait_failed = WAIT_FAILED_;

BOOST_CONSTEXPR_OR_CONST DWORD_ max_non_infinite_wait = (DWORD_)0xFFFFFFFE;

}
}

#include <boost/winapi/detail/footer.hpp>

#endif // BOOST_WINAPI_WAIT_CONSTANTS_HPP_INCLUDED_
