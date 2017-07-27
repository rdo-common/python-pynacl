%bcond_without check

%global modname pynacl

Name:           python-%{modname}
Version:        1.1.2
Release:        2%{?dist}
Summary:        Python binding to the Networking and Cryptography (NaCl) library

License:        ASL 2.0
URL:            https://github.com/pyca/pynacl
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz

BuildRequires:  libsodium-devel

%global _description \
PyNaCl is a Python binding to the Networking and Cryptography library,\
a crypto library with the stated goal of improving usability, security\
and speed.

%description %{_description}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-cffi
%if %{with check}
BuildRequires:  python2-pytest
BuildRequires:  python2-six
%endif
Requires:       python2-six
Requires:       python2-cffi

%description -n python2-%{modname} %{_description}

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cffi
%if %{with check}
BuildRequires:  python3-pytest
BuildRequires:  python3-six
%endif
Requires:       python3-six
Requires:       python3-cffi

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}
# Remove bundled libsodium, to be sure
rm -vrf src/libsodium/

%build
export SODIUM_INSTALL=system
%py2_build
%py3_build

%install
%py2_install
%py3_install

%if %{with check}
%check
PYTHONPATH=%{buildroot}%{python2_sitearch} py.test-%{python2_version} -v
PYTHONPATH=%{buildroot}%{python3_sitearch} py.test-%{python3_version} -v
%endif

%files -n python2-%{modname}
%license LICENSE
%doc README.rst
%{python2_sitearch}/PyNaCl-*.egg-info/
%{python2_sitearch}/nacl/

%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/PyNaCl-*.egg-info/
%{python3_sitearch}/nacl/

%changelog
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 01 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.1.2-1
- Update to 1.1.2

* Thu Mar 16 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuild for Python 3.6

* Mon Dec 19 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.1-1
- Initial package
