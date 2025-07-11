Name:		texlive-ruhyphen
Version:	21081
Release:	2
Summary:	Russian hyphenation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/hyphenation/ruhyphen
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ruhyphen.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ruhyphen.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of Russian hyphenation patterns supporting a
number of Cyrillic font encodings, including T2, UCY (Omega
Unicode Cyrillic), LCY, LWN (OT2), and koi8-r.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/ruhyphen/catkoi.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryoal.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryoas.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryoct.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryodv.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryomg.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryovl.tex
%{_texmfdistdir}/tex/generic/ruhyphen/cyryozn.tex
%{_texmfdistdir}/tex/generic/ruhyphen/enrhm2.tex
%{_texmfdistdir}/tex/generic/ruhyphen/hypht2.tex
%{_texmfdistdir}/tex/generic/ruhyphen/koi2koi.tex
%{_texmfdistdir}/tex/generic/ruhyphen/koi2lcy.tex
%{_texmfdistdir}/tex/generic/ruhyphen/koi2ot2.tex
%{_texmfdistdir}/tex/generic/ruhyphen/koi2t2a.tex
%{_texmfdistdir}/tex/generic/ruhyphen/koi2ucy.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruenhyph.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphal.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphas.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphct.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphdv.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphen.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphmg.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphvl.tex
%{_texmfdistdir}/tex/generic/ruhyphen/ruhyphzn.tex
#- source
%doc %{_texmfdistdir}/source/generic/ruhyphen/BUGS
%doc %{_texmfdistdir}/source/generic/ruhyphen/Makefile
%doc %{_texmfdistdir}/source/generic/ruhyphen/README
%doc %{_texmfdistdir}/source/generic/ruhyphen/README.ruhyphal
%doc %{_texmfdistdir}/source/generic/ruhyphen/hyphen.rules
%doc %{_texmfdistdir}/source/generic/ruhyphen/mkcyryo
%doc %{_texmfdistdir}/source/generic/ruhyphen/reduce-patt
%doc %{_texmfdistdir}/source/generic/ruhyphen/sorthyph
%doc %{_texmfdistdir}/source/generic/ruhyphen/sortkoi8
%doc %{_texmfdistdir}/source/generic/ruhyphen/trans

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex source %{buildroot}%{_texmfdistdir}
