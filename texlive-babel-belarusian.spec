Name:		texlive-babel-belarusian
Version:	49022
Release:	2
Summary:	Babel support for Belarusian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-belarusian
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-belarusian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-belarusian.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-belarusian.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for use of Babel in documents
written in Belarusian.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/babel-belarusian
%{_texmfdistdir}/tex/generic/babel-belarusian
%doc %{_texmfdistdir}/doc/generic/babel-belarusian

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
