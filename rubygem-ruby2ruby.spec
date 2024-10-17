%define oname ruby2ruby

Summary:    Allows generating pure ruby code easily from RubyParser compatible Sexps
Name:       rubygem-%{oname}
Version:    1.2.5
Release:    2
Group:      Development/Ruby
License:    MIT
URL:        https://seattlerb.rubyforge.org/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
Requires:   rubygem(sexp_processor) >= 3.0 
Requires:   rubygem(ruby_parser) >= 2.0
Requires:   rubygem(rubyforge) >= 2.0.4
Requires:   rubygem(minitest) >= 1.7.1
Requires:   rubygem(ParseTree) >= 3.0
Requires:   rubygem(hoe) >= 2.6.2
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
ruby2ruby provides a means of generating pure ruby code easily from
RubyParser compatible Sexps. This makes making dynamic language
processors in ruby easier than ever!

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x
ruby -pi -e 'sub(/\/usr\/local\/bin\/ruby/, "/usr/bin/env ruby")' %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/test/*
chmod 644 %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/{test,lib}/*
chmod 755 %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin/*

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{_bindir}/r2r_show
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.autotest
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Manifest.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.txt
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Sun Oct 10 2010 Rémy Clouard <shikamaru@mandriva.org> 1.2.5-1mdv2011.0
+ Revision: 584525
- import rubygem-ruby2ruby

