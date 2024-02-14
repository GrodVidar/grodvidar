from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Column


COUNTRIES = [("AF", "Afghanistan"), ("AX", "Aland Islands"), ("AL", "Albania"), ("DZ", "Algeria"), ("AS", "American Samoa"), ("AD", "Andorra"), ("AO", "Angola"), ("AI", "Anguilla"), ("AG", "Antigua and Barbuda"), ("AR", "Argentina"), ("AM", "Armenia"), ("AW", "Aruba"), ("AU", "Australia"), ("AT", "Austria"), ("AZ", "Azerbaijan"), ("BS", "Bahamas"), ("BH", "Bahrain"), ("BD", "Bangladesh"), ("BB", "Barbados"), ("BY", "Belarus"), ("BE", "Belgium"), ("BZ", "Belize"), ("BJ", "Benin"), ("BM", "Bermuda"), ("BT", "Bhutan"), ("BO", "Bolivia"), ("BA", "Bosnia and Herzegovina"), ("BW", "Botswana"), ("BR", "Brazil"), ("IO", "British Indian Ocean Territory"), ("BN", "Brunei Darussalam"), ("BG", "Bulgaria"), ("BF", "Burkina Faso"), ("BI", "Burundi"), ("CV", "Cabo Verde"), ("KH", "Cambodia"), ("CM", "Cameroon"), ("CA", "Canada"), ("KY", "Cayman Islands"), ("CF", "Central African Republic"), ("TD", "Chad"), ("CL", "Chile"), ("CN", "China"), ("CX", "Christmas Island"), ("CC", "Cocos (Keeling) Islands"), ("CO", "Colombia"), ("KM", "Comoros"), ("CK", "Cook Islands"), ("CR", "Costa Rica"), ("HR", "Croatia"), ("CU", "Cuba"), ("CW", "Curaçao"), ("CY", "Cyprus"), ("CZ", "Czech Republic"), ("CI", "Côte d'Ivoire"), ("CD", "Democratic Republic of the Congo"), ("DK", "Denmark"), ("DJ", "Djibouti"), ("DM", "Dominica"), ("DO", "Dominican Republic"), ("EC", "Ecuador"), ("EG", "Egypt"), ("SV", "El Salvador"), ("GQ", "Equatorial Guinea"), ("ER", "Eritrea"), ("EE", "Estonia"), ("ET", "Ethiopia"), ("FK", "Falkland Islands"), ("FO", "Faroe Islands"), ("FM", "Federated States of Micronesia"), ("FJ", "Fiji"), ("FI", "Finland"), ("MK", "Former Yugoslav Republic of Macedonia"), ("FR", "France"), ("PF", "French Polynesia"), ("GA", "Gabon"), ("GM", "Gambia"), ("GE", "Georgia"), ("DE", "Germany"), ("GH", "Ghana"), ("GI", "Gibraltar"), ("GR", "Greece"), ("GL", "Greenland"), ("GD", "Grenada"), ("GU", "Guam"), ("GT", "Guatemala"), ("GG", "Guernsey"), ("GN", "Guinea"), ("GW", "Guinea-Bissau"), ("GY", "Guyana"), ("HT", "Haiti"), ("VA", "Holy See"), ("HN", "Honduras"), ("HK", "Hong Kong"), ("HU", "Hungary"), ("IS", "Iceland"), ("IN", "India"), ("ID", "Indonesia"), ("IR", "Iran"), ("IQ", "Iraq"), ("IE", "Ireland"), ("IM", "Isle of Man"), ("IL", "Israel"), ("IT", "Italy"), ("JM", "Jamaica"), ("JP", "Japan"), ("JE", "Jersey"), ("JO", "Jordan"), ("KZ", "Kazakhstan"), ("KE", "Kenya"), ("KI", "Kiribati"), ("KW", "Kuwait"), ("KG", "Kyrgyzstan"), ("LA", "Laos"), ("LV", "Latvia"), ("LB", "Lebanon"), ("LS", "Lesotho"), ("LR", "Liberia"), ("LY", "Libya"), ("LI", "Liechtenstein"), ("LT", "Lithuania"), ("LU", "Luxembourg"), ("MO", "Macau"), ("MG", "Madagascar"), ("MW", "Malawi"), ("MY", "Malaysia"), ("MV", "Maldives"), ("ML", "Mali"), ("MT", "Malta"), ("MH", "Marshall Islands"), ("MQ", "Martinique"), ("MR", "Mauritania"), ("MU", "Mauritius"), ("MX", "Mexico"), ("MD", "Moldova"), ("MC", "Monaco"), ("MN", "Mongolia"), ("ME", "Montenegro"), ("MS", "Montserrat"), ("MA", "Morocco"), ("MZ", "Mozambique"), ("MM", "Myanmar"), ("NA", "Namibia"), ("NR", "Nauru"), ("NP", "Nepal"), ("NL", "Netherlands"), ("NZ", "New Zealand"), ("NI", "Nicaragua"), ("NE", "Niger"), ("NG", "Nigeria"), ("NU", "Niue"), ("NF", "Norfolk Island"), ("KP", "North Korea"), ("MP", "Northern Mariana Islands"), ("NO", "Norway"), ("OM", "Oman"), ("PK", "Pakistan"), ("PW", "Palau"), ("PA", "Panama"), ("PG", "Papua New Guinea"), ("PY", "Paraguay"), ("PE", "Peru"), ("PH", "Philippines"), ("PN", "Pitcairn"), ("PL", "Poland"), ("PT", "Portugal"), ("PR", "Puerto Rico"), ("QA", "Qatar"), ("CG", "Republic of the Congo"), ("RO", "Romania"), ("RU", "Russia"), ("RW", "Rwanda"), ("BL", "Saint Barthélemy"), ("KN", "Saint Kitts and Nevis"), ("LC", "Saint Lucia"), ("VC", "Saint Vincent and the Grenadines"), ("WS", "Samoa"), ("SM", "San Marino"), ("ST", "Sao Tome and Principe"), ("SA", "Saudi Arabia"), ("SN", "Senegal"), ("RS", "Serbia"), ("SC", "Seychelles"), ("SL", "Sierra Leone"), ("SG", "Singapore"), ("SX", "Sint Maarten"), ("SK", "Slovakia"), ("SI", "Slovenia"), ("SB", "Solomon Islands"), ("SO", "Somalia"), ("ZA", "South Africa"), ("KR", "South Korea"), ("SS", "South Sudan"), ("ES", "Spain"), ("LK", "Sri Lanka"), ("PS", "State of Palestine"), ("SD", "Sudan"), ("SR", "Suriname"), ("SZ", "Swaziland"), ("SE", "Sweden"), ("CH", "Switzerland"), ("SY", "Syrian Arab Republic"), ("TW", "Taiwan"), ("TJ", "Tajikistan"), ("TZ", "Tanzania"), ("TH", "Thailand"), ("TL", "Timor-Leste"), ("TG", "Togo"), ("TK", "Tokelau"), ("TO", "Tonga"), ("TT", "Trinidad and Tobago"), ("TN", "Tunisia"), ("TR", "Turkey"), ("TM", "Turkmenistan"), ("TC", "Turks and Caicos Islands"), ("TV", "Tuvalu"), ("UG", "Uganda"), ("UA", "Ukraine"), ("AE", "United Arab Emirates"), ("GB", "United Kingdom"), ("US", "United States of America"), ("UY", "Uruguay"), ("UZ", "Uzbekistan"), ("VU", "Vanuatu"), ("VE", "Venezuela"), ("VN", "Vietnam"), ("VG", "Virgin Islands (British)"), ("VI", "Virgin Islands (U.S.)"), ("EH", "Western Sahara"), ("YE", "Yemen"), ("ZM", "Zambia"), ("ZW", "Zimbabwe")]

NETFLIX = 'netflix'
PRIME = 'amazonprimevideo'
DISNEY_PLUS = 'disneyplus'
VIAPLAY = 'viaplay'
HBO_MAX = 'hbomax'
SKY_SHOWTIME = 'skyshowtime'
SF_ANYTIME = 'sfanytime'
PROVIDER_CHOICES = (
    (NETFLIX, 'Netflix'),
    (PRIME, 'Amazon Prime Video'),
    (DISNEY_PLUS, 'Disney+'),
    (VIAPLAY, 'Viaplay'),
    (HBO_MAX, 'HBO Max'),
    (SKY_SHOWTIME, 'Sky Showtime'),
    (SF_ANYTIME, 'SF Anytime'),
)


class MoviesForm(forms.Form):

    providers = forms.MultipleChoiceField(
        label='',
        choices=PROVIDER_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )

    country = forms.ChoiceField(
        label='',
        widget=forms.Select(
            attrs={
                'class': 'select2Field',
            }
        ),
        choices=COUNTRIES,
    )

    title = forms.CharField(
        label='',
        max_length=100,
        min_length=3,
        widget=forms.TextInput(attrs={'placeholder': 'Title'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                'country',
                css_class="px-5",
            ),
            Row(
                Column('title'),
                Column(Submit('submit', 'Go!', css_class='btn btn-dark')),
                css_class="px-5",
            )
        )

