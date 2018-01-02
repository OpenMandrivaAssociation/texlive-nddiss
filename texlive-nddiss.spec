Name:		texlive-nddiss
Version:	3.2017.2
Release:	1
Summary:	Notre Dame Dissertation format class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nddiss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nddiss.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nddiss.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nddiss.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
