Name:		texlive-zref
Version:	68278
Release:	1
Summary:	A new reference scheme for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zref
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zref.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zref.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package offers a means to remove the limitation, of only
two properties, that is inherent in the way LaTeX's reference
system works. The package implements an extensible referencing
system, where properties may be defined and used in the course
of a document. It provides an interface for macro programmers
to access the new reference scheme and some modules that use
it. Modules available are: zref-user, use zref for
"traditional" labels and references; zref-abspage, retrieve
absolute page numbers (physical pages, as opposed to the
'logical' page number that is normally typeset when a page
number is requested; zref-lastpage, provide a zref-label for
the last page of the document; zref-nextpage, provide the page
number of the next page of the document; zref-totpages, provide
the total number of pages in the document; zref-pagelayout,
provide the page layout parameters of a each page (which may
then be printed at the end of the document); zref-perpage, make
a counter reset for each new page; zref-titleref, make section
title or caption text available through the reference system;
zref-savepos, make positions on a page available; zref-dotfill,
controlled dot-filling; zref-env, record the latest
environment's name and the line it started on; and zref-xr,
provide the facilities of the xr and xr-hyper packages.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/zref
%{_texmfdistdir}/tex/latex/zref
%doc %{_texmfdistdir}/doc/latex/zref

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
