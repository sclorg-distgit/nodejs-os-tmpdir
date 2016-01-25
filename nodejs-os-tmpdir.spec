%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}

# ava is not in fedora yet
%global enable_tests 0
%global module_name os-tmpdir
%global gittag0 1.0.1

%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        %{gittag0}
Release:        3%{?dist}
Summary:        Node.js os.tmpdir() ponyfill

License:        MIT
URL:            https://github.com/sindresorhus/os-tmpdir
Source0:        https://github.com/sindresorhus/%{module_name}/archive/%{gittag0}.tar.gz#/%{module_name}-%{gittag0}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires: %{?scl_prefix}npm(ava)
%endif

%description
%{summary}.

%prep
%setup -q -n %{module_name}-%{gittag0}
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
node test.js
%endif

%files
%doc readme.md license
%{nodejs_sitelib}/%{module_name}

%changelog
* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-3
- Enable scl macros

* Sat Sep 12 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.1-1
- Initial packaging
