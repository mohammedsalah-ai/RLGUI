from elements.env_dialog.ui_env_dialog import Ui_EnvDialog
from PySide6.QtWidgets import QDialog

from components.md_widget import MDWidget


class EnvDialog(QDialog, Ui_EnvDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.md_widget = MDWidget()
        self.md_widget.setMD(
            """
            # Videt audax

## Orbe quaecumque alebat docta propago semper alii

Lorem markdownum novem sed dedere undis: longa iam praesagaque, primum, arma nec
videt ponunt profuit: meo. Honor [et Pelasgos](http://nisi.org/) in fuerat in
subit laniavit, opacas volenti arma. Formae *pressos emittere licet* praemia
silvis! Iram nisi vaccae posse **pavidus**. Iuppiter erat; dis est liquit
veniunt, est ipsa.

- Pastae pennis naturaeque saetiger
- Ut passu
- In imperio facibus hic tecta quae praesens
- Mors conexa indeploratum super pantherarum
- Et quos
- Artus fraudes

## Cursus venere est

Dicente numerum suo aeris, gemit et fuit post, referre redimitus, praemia.
Mearum mihi *tremat* somno. Vina tutam nate circumfert illi hoc quae limina
mersit colla. Oblita distinctus Achaica virum et retemptat longo amplexuque
summam descendit flemus ocius medias geminae? Deserto ramos velamina umbras
maris *quae* non cycnorum, e [ne locus](http://exilio.com/) rurigenae coniunx,
nominat *illa deceptam*.

1. Dubitavit loquentem Italiam
2. Posce vindicat eripuit nudos quacumque parari stare
3. Perseus pectora

## Minyae coegi operosa ergo timida cupidine Thaumantias

Pro non obsessa meis reges, adfixa Nereusque *sedibus nescit Capitolia* aut.
Datis usus omni delere: hunc negata agmine quadriiugi Colchis aut
[aeratas](http://www.pignusquepetis.net/filianon.html) facinus. Turba nisi
[tanti urbis ferox](http://abstulitausum.net/) obortis: sustulit merito est
frater et antemnae exstabant Apollinei auctor Atlantis vicimus Macareus
[manus](http://quae.net/). Mensae fit est Calydonius virtute habent adsueto me
ventis mitissima Peneide: et illo invitusque **ferox huc**. In dat Galanthida
tardae silices tractu odore solus me eademque litore: si, opto qui tempora
potest caeruleusque.

    web_kilobyte_document(batch_thick_serial, 4 + dropPersonal +
            rdramArtificialKindle, archieDefinition.software(3, scroll,
            spreadsheet_meta_read));
    search += webmailAspMode(wddmUps + scroll);
    if (gigabyte < display) {
        menu.lcd_adf(jsfTarget);
    } else {
        template_system = 71;
        memorySpoofing *= numQueryType + file(search_ad, computerEbook);
        itunes_ivr = directx_commercial_speakers(virusNativeSearch, alert,
                copyright);
    }

Haec maduere respice: super *corpora mandata Dixit* restabat dixerit frustraque
hostes. Arma amore, *pulcherrima*, fecundaque aevum nec si istis, pro huc
Letoia: in festum nigrescere. Ante concretum at solebat addidit, furialiaque
omni ficta, non ne suis, quas possem o choreas exsistunt ferunt.

            """
        )

        self.envDescriptionScrollArea.setWidget(self.md_widget)
