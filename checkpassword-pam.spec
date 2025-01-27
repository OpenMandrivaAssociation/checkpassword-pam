Summary:	A checkpassword compatible authentication program
Name:		checkpassword-pam
Version:	0.99
Release:	8
License:	GPL
Group:		System/Servers
URL:		https://checkpasswd-pam.sourceforge.net/
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	pam-devel
Provides:	checkpassword
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
checkpassword-pam is an implementation of checkpassword-compatible
authentication program.

Checkpassword is described in <URL:http://cr.yp.to/checkpwd.html>

checkpassword-pam was written from scratch.  There are several older
packages called checkpassword-pam, derived from DJB's checkpassword
code.   This checkpassword-pam is more modern and
administrator-friendly.


If you are using Linux-PAM, make sure it is more recent than 0.59.
Incompatibilities are in the PAM conversation function (number of
requests vs number of responses).  All modern Linux distribution use
PAM newer than that.

%prep

%setup -q

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}/bin
install -d %{buildroot}%{_sysconfdir}/pam.d
install -d %{buildroot}%{_mandir}/man8

install -m755 checkpassword-pam %{buildroot}/bin/
install -m644 checkpassword-pam.8 %{buildroot}%{_mandir}/man8/

# This is taken from %{_sysconfdir}/pam.d/login
# I hope this is sufficent?

cat > %{buildroot}%{_sysconfdir}/pam.d/checkpassword-pam << EOF
#%PAM-1.0
auth       required	pam_securetty.so
auth       include      system-auth
auth       required	pam_nologin.so
account    include      system-auth
password   include      system-auth
session    include      system-auth
session    optional	pam_console.so
EOF

chmod 644 %{buildroot}%{_sysconfdir}/pam.d/checkpassword-pam

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS NEWS README interface.html
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/checkpassword-pam
%attr(755,root,root) /bin/checkpassword-pam
%attr(644,root,root) %{_mandir}/man8/checkpassword-pam.8*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.99-7mdv2011.0
+ Revision: 616998
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.99-6mdv2010.0
+ Revision: 424826
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.99-5mdv2009.0
+ Revision: 243869
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.99-3mdv2008.1
+ Revision: 140692
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires obsoletes buildprereq


* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 0.99-3mdv2007.0
+ Revision: 113774
- Import checkpassword-pam

* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 0.99-3mdv2007.1
- fix pam

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 0.99-2mdk
- rebuild

* Sat Nov 13 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.99-1mdk
- 0.99

