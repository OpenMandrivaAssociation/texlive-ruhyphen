%global tl_name ruhyphen
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Russian hyphenation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/ruhyphen
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ruhyphen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ruhyphen.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of Russian hyphenation patterns supporting a number of
Cyrillic font encodings, including T2, UCY (Omega Unicode Cyrillic),
LCY, LWN (OT2), and koi8-r.

