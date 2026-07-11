%global tl_name babel-belarusian
%global tl_revision 49022

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5
Release:	%{tl_revision}.1
Summary:	Babel support for Belarusian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/belarusian
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-belarusian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-belarusian.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-belarusian.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for use of Babel in documents written in
Belarusian.

