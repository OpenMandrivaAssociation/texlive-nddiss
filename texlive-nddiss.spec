Name:		texlive-nddiss
Version:	45107
Release:	1
Summary:	Notre Dame Dissertation format class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nddiss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nddiss.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nddiss.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nddiss.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class file conforms to the requirements of the Graduate
School of the University of Notre Dame; with it a user can
format a thesis or dissertation in LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/nddiss
%{_texmfdistdir}/tex/latex/nddiss
%doc %{_texmfdistdir}/doc/latex/nddiss
#- source
%doc %{_texmfdistdir}/source/latex/nddiss

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
