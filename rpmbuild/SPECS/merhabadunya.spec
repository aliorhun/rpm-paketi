Name:       merhabadunya
Version:    0.10
Release:    1
Summary:    Temel RPM paketi
License:    GPLv2
Packager:   Ali Orhun Akkirman
Requires:   bash

%description
Örnek ve basit bir RPM paketi

%prep
# hazırlık içerikleri

%pre
# yükleme öncesi yapılacak betikler

%post
# yükleme sonrası yapılacak betikler

%build
cat > merhabadunya.sh <<EOF
#!/usr/bin/bash
echo "Merhaba Dünya"
EOF

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 merhabadunya.sh %{buildroot}/usr/bin/merhabadunya

%files
/usr/bin/merhabadunya

%changelog
# degisenler
