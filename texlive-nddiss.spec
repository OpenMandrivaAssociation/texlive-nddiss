# revision 29349
# category Package
# catalog-ctan /macros/latex/contrib/nddiss
# catalog-date 2012-07-17 16:43:33 +0200
# catalog-license lppl
# catalog-version 3.0
Name:		texlive-nddiss
Version:	3.0
Release:	10
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
%{_texmfdistdir}/bibtex/bst/nddiss/nddiss2e.bst
%{_texmfdistdir}/tex/latex/nddiss/nddiss2e.cls
%doc %{_texmfdistdir}/doc/latex/nddiss/ReadMe.1st.txt
%doc %{_texmfdistdir}/doc/latex/nddiss/example-v1.3/LICENSE
%doc %{_texmfdistdir}/doc/latex/nddiss/example-v1.3/README.1st.txt
%doc %{_texmfdistdir}/doc/latex/nddiss/example-v1.3/VERSION
%doc %{_texmfdistdir}/doc/latex/nddiss/example-v1.3/appendix.tex
%doc %{_texmfdistdir}/doc/latex/nddiss/example-v1.3/chapter1.tex
%doc %{_texmfdistdir}/doc/latex/nddiss/example-v1.3/chapter2.tex
%doc %{_texmfdistdir}/doc/latex/nddiss/example-v1.3/example.bib
%doc %{_texmfdistdir}/doc/latex/nddiss/example-v1.3/example.pdf
%doc %{_texmfdistdir}/doc/latex/nddiss/example-v1.3/example.tex
%doc %{_texmfdistdir}/doc/latex/nddiss/example-v1.3/makefile
%doc %{_texmfdistdir}/doc/latex/nddiss/example-v1.3/makefile.chapterbib
%doc %{_texmfdistdir}/doc/latex/nddiss/example-v1.3/sample_nd.eps
%doc %{_texmfdistdir}/doc/latex/nddiss/example-v1.3/sample_nd.pdf
%doc %{_texmfdistdir}/doc/latex/nddiss/ltxdoc.cfg
%doc %{_texmfdistdir}/doc/latex/nddiss/nddiss2e.pdf
%doc %{_texmfdistdir}/doc/latex/nddiss/process.sh
%doc %{_texmfdistdir}/doc/latex/nddiss/template.tex
#- source
%doc %{_texmfdistdir}/source/latex/nddiss/nddiss2e.dtx
%doc %{_texmfdistdir}/source/latex/nddiss/nddiss2e.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
