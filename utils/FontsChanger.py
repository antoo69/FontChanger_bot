
from pprint import pprint


# Fonts Ro'yxati
fonts_lst = [
    'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890',
    '𝔄𝔞𝔅𝔟ℭ𝔠𝔇𝔡𝔈𝔢𝔉𝔣𝔊𝔤ℌ𝔥ℑ𝔦𝔍𝔧𝔎𝔨𝔏𝔩𝔐𝔪𝔑𝔫𝔒𝔬𝔓𝔭𝔔𝔮ℜ𝔯𝔖𝔰𝔗𝔱𝔘𝔲𝔙𝔳𝔚𝔴𝔛𝔵𝔜𝔶ℨ𝔷1234567890',
    '𝕬𝖆𝕭𝖇𝕮𝖈𝕯𝖉𝕰𝖊𝕱𝖋𝕲𝖌𝕳𝖍𝕴𝖎𝕵𝖏𝕶𝖐𝕷𝖑𝕸𝖒𝕹𝖓𝕺𝖔𝕻𝖕𝕼𝖖𝕽𝖗𝕾𝖘𝕿𝖙𝖀𝖚𝖁𝖛𝖂𝖜𝖃𝖝𝖄𝖞𝖅𝖟1234567890',
    '𝔸𝕒𝔹𝕓ℂ𝕔𝔻𝕕𝔼𝕖𝔽𝕗𝔾𝕘ℍ𝕙𝕀𝕚𝕁𝕛𝕂𝕜𝕃𝕝𝕄𝕞ℕ𝕟𝕆𝕠ℙ𝕡ℚ𝕢ℝ𝕣𝕊𝕤𝕋𝕥𝕌𝕦𝕍𝕧𝕎𝕨𝕏𝕩𝕐𝕪ℤ𝕫𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘',
    '𝒜𝒶ℬ𝒷𝒞𝒸𝒟𝒹ℰℯℱ𝒻𝒢ℊℋ𝒽ℐ𝒾𝒥𝒿𝒦𝓀ℒ𝓁ℳ𝓂𝒩𝓃𝒪ℴ𝒫𝓅𝒬𝓆ℛ𝓇𝒮𝓈𝒯𝓉𝒰𝓊𝒱𝓋𝒲𝓌𝒳𝓍𝒴𝓎𝒵𝓏1234567890',
    '𝓐𝓪𝓑𝓫𝓒𝓬𝓓𝓭𝓔𝓮𝓕𝓯𝓖𝓰𝓗𝓱𝓘𝓲𝓙𝓳𝓚𝓴𝓛𝓵𝓜𝓶𝓝𝓷𝓞𝓸𝓟𝓹𝓠𝓺𝓡𝓻𝓢𝓼𝓣𝓽𝓤𝓾𝓥𝓿𝓦𝔀𝓧𝔁𝓨𝔂𝓩𝔃1234567890',
    '𝙰𝚊𝙱𝚋𝙲𝚌𝙳𝚍𝙴𝚎𝙵𝚏𝙶𝚐𝙷𝚑𝙸𝚒𝙹𝚓𝙺𝚔𝙻𝚕𝙼𝚖𝙽𝚗𝙾𝚘𝙿𝚙𝚀𝚚𝚁𝚛𝚂𝚜𝚃𝚝𝚄𝚞𝚅𝚟𝚆𝚠𝚇𝚡𝚈𝚢𝚉𝚣𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶',
    'ⒶⓐⒷⓑⒸⓒⒹⓓⒺⓔⒻⓕⒼⓖⒽⓗⒾⓘⒿⓙⓀⓚⓁⓛⓂⓜⓃⓝⓄⓞⓅⓟⓆⓠⓇⓡⓈⓢⓉⓣⓊⓤⓋⓥⓌⓦⓍⓧⓎⓨⓏⓩ①②③④⑤⑥⑦⑧⑨⓪',
    '🅐🅐🅑🅑🅒🅒🅓🅓🅔🅔🅕🅕🅖🅖🅗🅗🅘🅘🅙🅙🅚🅚🅛🅛🅜🅜🅝🅝🅞🅞🅟🅟🅠🅠🅡🅡🅢🅢🅣🅣🅤🅤🅥🅥🅦🅦🅧🅧🅨🅨🅩🅩➊➋➌➍➎➏➐➑➒⓿',
    '🄰🄰🄱🄱🄲🄲🄳🄳🄴🄴🄵🄵🄶🄶🄷🄷🄸🄸🄹🄹🄺🄺🄻🄻🄼🄼🄽🄽🄾🄾🄿🄿🅀🅀🅁🅁🅂🅂🅃🅃🅄🅄🅅🅅🅆🅆🅇🅇🅈🅈🅉🅉1234567890',
    '🅰🅰🅱🅱🅲🅲🅳🅳🅴🅴🅵🅵🅶🅶🅷🅷🅸🅸🅹🅹🅺🅺🅻🅻🅼🅼🅽🅽🅾🅾🅿🅿🆀🆀🆁🆁🆂🆂🆃🆃🆄🆄🆅🆅🆆🆆🆇🆇🆈🆈🆉🆉1234567890',
    '🇦 🇦 🇧 🇧 🇨 🇨 🇩 🇩 🇪 🇪 🇫 🇫 🇬 🇬 🇭 🇭 🇮 🇮 🇯 🇯 🇰 🇰 🇱 🇱 🇲 🇲 🇳 🇳 🇴 🇴 🇵 🇵 🇶 🇶 🇷 🇷 🇸 🇸 🇹 🇹 🇺 🇺 🇻 🇻 🇼 🇼 🇽 🇽 🇾 🇾 🇿 🇿 1 2 3 4 5 6 7 8 9 0 ',
    '𝗔𝗮𝗕𝗯𝗖𝗰𝗗𝗱𝗘𝗲𝗙𝗳𝗚𝗴𝗛𝗵𝗜𝗶𝗝𝗷𝗞𝗸𝗟𝗹𝗠𝗺𝗡𝗻𝗢𝗼𝗣𝗽𝗤𝗾𝗥𝗿𝗦𝘀𝗧𝘁𝗨𝘂𝗩𝘃𝗪𝘄𝗫𝘅𝗬𝘆𝗭𝘇𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬',
    '𝘼𝙖𝘽𝙗𝘾𝙘𝘿𝙙𝙀𝙚𝙁𝙛𝙂𝙜𝙃𝙝𝙄𝙞𝙅𝙟𝙆𝙠𝙇𝙡𝙈𝙢𝙉𝙣𝙊𝙤𝙋𝙥𝙌𝙦𝙍𝙧𝙎𝙨𝙏𝙩𝙐𝙪𝙑𝙫𝙒𝙬𝙓𝙭𝙔𝙮𝙕𝙯𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎',
    '𝘈𝘢𝘉𝘣𝘊𝘤𝘋𝘥𝘌𝘦𝘍𝘧𝘎𝘨𝘏𝘩𝘐𝘪𝘑𝘫𝘒𝘬𝘓𝘭𝘔𝘮𝘕𝘯𝘖𝘰𝘗𝘱𝘘𝘲𝘙𝘳𝘚𝘴𝘛𝘵𝘜𝘶𝘝𝘷𝘞𝘸𝘟𝘹𝘠𝘺𝘡𝘻1234567890',
    '𝐴𝑎𝐵𝑏𝐶𝑐𝐷𝑑𝐸𝑒𝐹𝑓𝐺𝑔𝐻ℎ𝐼𝑖𝐽𝑗𝐾𝑘𝐿𝑙𝑀𝑚𝑁𝑛𝑂𝑜𝑃𝑝𝑄𝑞𝑅𝑟𝑆𝑠𝑇𝑡𝑈𝑢𝑉𝑣𝑊𝑤𝑋𝑥𝑌𝑦𝑍𝑧1234567890',
    '𝑨𝒂𝑩𝒃𝑪𝒄𝑫𝒅𝑬𝒆𝑭𝒇𝑮𝒈𝑯𝒉𝑰𝒊𝑱𝒋𝑲𝒌𝑳𝒍𝑴𝒎𝑵𝒏𝑶𝒐𝑷𝒑𝑸𝒒𝑹𝒓𝑺𝒔𝑻𝒕𝑼𝒖𝑽𝒗𝑾𝒘𝑿𝒙𝒀𝒚𝒁𝒛𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎',
    '𝐀𝐚𝐁𝐛𝐂𝐜𝐃𝐝𝐄𝐞𝐅𝐟𝐆𝐠𝐇𝐡𝐈𝐢𝐉𝐣𝐊𝐤𝐋𝐥𝐌𝐦𝐍𝐧𝐎𝐨𝐏𝐩𝐐𝐪𝐑𝐫𝐒𝐬𝐓𝐭𝐔𝐮𝐕𝐯𝐖𝐰𝐗𝐱𝐘𝐲𝐙𝐳𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎',
    'ᵃᵃᵇᵇᶜᶜᵈᵈᵉᵉᶠᶠᵍᵍʰʰⁱⁱʲʲᵏᵏˡˡᵐᵐⁿⁿᵒᵒᵖᵖᵠᵠʳʳˢˢᵗᵗᵘᵘᵛᵛʷʷˣˣʸʸᶻᶻ¹²³⁴⁵⁶⁷⁸⁹⁰',
    'ᴀᴀʙʙᴄᴄᴅᴅᴇᴇꜰꜰɢɢʜʜɪɪᴊᴊᴋᴋʟʟᴍᴍɴɴᴏᴏᴘᴘQQʀʀꜱꜱᴛᴛᴜᴜᴠᴠᴡᴡxxʏʏᴢᴢ1234567890',
    'ＡａＢｂＣｃＤｄＥｅＦｆＧｇＨｈＩｉＪｊＫｋＬｌＭｍＮｎＯｏＰｐＱｑＲｒＳｓＴｔＵｕＶｖＷｗＸｘＹｙＺｚ１２３４５６７８９０',
    'ααճճccժժҽҽբբցցհհííյյkkllตตղղօօթթզզɾɾssԵԵմմѵѵաաxxվվzz1234567890',
    'ԹԹՅՅՇՇԺԺeeԲԲԳԳɧɧɿɿʝʝkkʅʅʍʍՌՌԾԾρρφφՐՐՏՏԵԵՄՄעעաաՃՃՎՎՀՀ1234567890',
    'ααႦႦƈƈԃԃҽҽϝϝɠɠԋԋιιʝʝƙƙʅʅɱɱɳɳσσρρϙϙɾɾʂʂƚƚυυʋʋɯɯxxყყȥȥ1234567890',
    'ǟǟɮɮƈƈɖɖɛɛʄʄɢɢɦɦɨɨʝʝӄӄʟʟʍʍռռօօքքզզʀʀֆֆȶȶʊʊʋʋաաӼӼʏʏʐʐ1234567890',
    'ᎪᎪbbᏟᏟᎠᎠᎬᎬffᎶᎶhhᎥᎥjjᏦᏦᏞᏞmmᏁᏁᎾᎾᏢᏢqqᏒᏒssᏆᏆuuᏉᏉᎳᎳxxᎽᎽᏃᏃ1234567890',
    '𝐀คᗷβ匚𝔠ᗪ𝒹𝓔𝐞𝓕千ﻮ𝔾𝕙Ⓗ𝐈𝐈ＪⓙҜкĻㄥ爪Μ𝔫Ň๏ⓄƤᑭợqⓇ𝓻ŜŞ𝐭𝓉ᑌⓊＶv𝔀𝓦𝓧ˣ𝓨𝕪zž❶２３４❺❻❼➇９ʘ',
    'A̼a̼B̼b̼C̼c̼D̼d̼E̼e̼F̼f̼G̼g̼H̼h̼I̼i̼J̼j̼K̼k̼L̼l̼M̼m̼N̼n̼O̼o̼P̼p̼Q̼q̼R̼r̼S̼s̼T̼t̼U̼u̼V̼v̼W̼w̼X̼x̼Y̼y̼Z̼z̼1̼2̼3̼4̼5̼6̼7̼8̼9̼0̼',
    'Ă̈ă̈B̆̈b̆̈C̆̈c̆̈D̆̈d̆̈Ĕ̈ĕ̈F̆̈f̆̈Ğ̈ğ̈H̆̈h̆̈Ĭ̈ĭ̈J̆̈j̆̈K̆̈k̆̈L̆̈l̆̈M̆̈m̆̈N̆̈n̆̈Ŏ̈ŏ̈P̆̈p̆̈Q̆̈q̆̈R̆̈r̆̈S̆̈s̆̈T̆̈t̆̈Ŭ̈ŭ̈V̆̈v̆̈W̆̈w̆̈X̆̈x̆̈Y̆̈y̆̈Z̆̈z̆̈1̆̈2̆̈3̆̈4̆̈5̆̈6̆̈7̆̈8̆̈9̆̈0̆̈',
    'Ȃ̈ȃ̈B̑̈b̑̈C̑̈c̑̈D̑̈d̑̈Ȇ̈ȇ̈F̑̈f̑̈G̑̈g̑̈H̑̈h̑̈Ȋ̈ȋ̈J̑̈j̑̈K̑̈k̑̈L̑̈l̑̈M̑̈m̑̈N̑̈n̑̈Ȏ̈ȏ̈P̑̈p̑̈Q̑̈q̑̈Ȓ̈ȓ̈S̑̈s̑̈T̑̈t̑̈Ȗ̈ȗ̈V̑̈v̑̈W̑̈w̑̈X̑̈x̑̈Y̑̈y̑̈Z̑̈z̑̈1̑̈2̑̈3̑̈4̑̈5̑̈6̑̈7̑̈8̑̈9̑̈0̑̈',
    'A͜͡a͜͡B͜͡b͜͡C͜͡c͜͡D͜͡d͜͡E͜͡e͜͡F͜͡f͜͡G͜͡g͜͡H͜͡h͜͡I͜͡i͜͡J͜͡j͜͡K͜͡k͜͡L͜͡l͜͡M͜͡m͜͡N͜͡n͜͡O͜͡o͜͡P͜͡p͜͡Q͜͡q͜͡R͜͡r͜͡S͜͡s͜͡T͜͡t͜͡U͜͡u͜͡V͜͡v͜͡W͜͡w͜͡X͜͡x͜͡Y͜͡y͜͡Z͜͡z͜͡1͜͡2͜͡3͜͡4͜͡5͜͡6͜͡7͜͡8͜͡9͜͡0͜͡',
    'A̾a̾B̾b̾C̾c̾D̾d̾E̾e̾F̾f̾G̾g̾H̾h̾I̾i̾J̾j̾K̾k̾L̾l̾M̾m̾N̾n̾O̾o̾P̾p̾Q̾q̾R̾r̾S̾s̾T̾t̾U̾u̾V̾v̾W̾w̾X̾x̾Y̾y̾Z̾z̾1̾2̾3̾4̾5̾6̾7̾8̾9̾0̾',
    'ḀͦḁͦB̥ͦb̥ͦC̥ͦc̥ͦD̥ͦd̥ͦE̥ͦe̥ͦF̥ͦf̥ͦG̥ͦg̥ͦH̥ͦh̥ͦI̥ͦi̥ͦJ̥ͦj̥ͦK̥ͦk̥ͦL̥ͦl̥ͦM̥ͦm̥ͦN̥ͦn̥ͦO̥ͦo̥ͦP̥ͦp̥ͦQ̥ͦq̥ͦR̥ͦr̥ͦS̥ͦs̥ͦT̥ͦt̥ͦU̥ͦu̥ͦV̥ͦv̥ͦW̥ͦw̥ͦX̥ͦx̥ͦY̥ͦy̥ͦZ̥ͦz̥ͦ1̥ͦ2̥ͦ3̥ͦ4̥ͦ5̥ͦ6̥ͦ7̥ͦ8̥ͦ9̥ͦ0̥ͦ',
    'A̲a̲B̲b̲C̲c̲D̲d̲E̲e̲F̲f̲G̲g̲H̲h̲I̲i̲J̲j̲K̲k̲L̲l̲M̲m̲N̲n̲O̲o̲P̲p̲Q̲q̲R̲r̲S̲s̲T̲t̲U̲u̲V̲v̲W̲w̲X̲x̲Y̲y̲Z̲z̲1̲2̲3̲4̲5̲6̲7̲8̲9̲0̲',
    'A͟a͟B͟b͟C͟c͟D͟d͟E͟e͟F͟f͟G͟g͟H͟h͟I͟i͟J͟j͟K͟k͟L͟l͟M͟m͟N͟n͟O͟o͟P͟p͟Q͟q͟R͟r͟S͟s͟T͟t͟U͟u͟V͟v͟W͟w͟X͟x͟Y͟y͟Z͟z͟1͟2͟3͟4͟5͟6͟7͟8͟9͟0͟',
    'A͛a͛B͛b͛C͛c͛D͛d͛E͛e͛F͛f͛G͛g͛H͛h͛I͛i͛J͛j͛K͛k͛L͛l͛M͛m͛N͛n͛O͛o͛P͛p͛Q͛q͛R͛r͛S͛s͛T͛t͛U͛u͛V͛v͛W͛w͛X͛x͛Y͛y͛Z͛z͛1͛2͛3͛4͛5͛6͛7͛8͛9͛0͛',
    'A͎a͎B͎b͎C͎c͎D͎d͎E͎e͎F͎f͎G͎g͎H͎h͎I͎i͎J͎j͎K͎k͎L͎l͎M͎m͎N͎n͎O͎o͎P͎p͎Q͎q͎R͎r͎S͎s͎T͎t͎U͎u͎V͎v͎W͎w͎X͎x͎Y͎y͎Z͎z͎1͎2͎3͎4͎5͎6͎7͎8͎9͎0͎',
    'A̺͆a̺͆B̺͆b̺͆C̺͆c̺͆D̺͆d̺͆E̺͆e̺͆F̺͆f̺͆G̺͆g̺͆H̺͆h̺͆I̺͆i̺͆J̺͆j̺͆K̺͆k̺͆L̺͆l̺͆M̺͆m̺͆N̺͆n̺͆O̺͆o̺͆P̺͆p̺͆Q̺͆q̺͆R̺͆r̺͆S̺͆s̺͆T̺͆t̺͆U̺͆u̺͆V̺͆v̺͆W̺͆w̺͆X̺͆x̺͆Y̺͆y̺͆Z̺͆z̺͆1̺͆2̺͆3̺͆4̺͆5̺͆6̺͆7̺͆8̺͆9̺͆0̺͆',
    'A͓̽a͓̽B͓̽b͓̽C͓̽c͓̽D͓̽d͓̽E͓̽e͓̽F͓̽f͓̽G͓̽g͓̽H͓̽h͓̽I͓̽i͓̽J͓̽j͓̽K͓̽k͓̽L͓̽l͓̽M͓̽m͓̽N͓̽n͓̽O͓̽o͓̽P͓̽p͓̽Q͓̽q͓̽R͓̽r͓̽S͓̽s͓̽T͓̽t͓̽U͓̽u͓̽V͓̽v͓̽W͓̽w͓̽X͓̽x͓̽Y͓̽y͓̽Z͓̽z͓̽1͓̽2͓̽3͓̽4͓̽5͓̽6͓̽7͓̽8͓̽9͓̽0͓̽',
    'A҉a҉B҉b҉C҉c҉D҉d҉E҉e҉F҉f҉G҉g҉H҉h҉I҉i҉J҉j҉K҉k҉L҉l҉M҉m҉N҉n҉O҉o҉P҉p҉Q҉q҉R҉r҉S҉s҉T҉t҉U҉u҉V҉v҉W҉w҉X҉x҉Y҉y҉Z҉z҉1҉2҉3҉4҉5҉6҉7҉8҉9҉0҉',
    'A҈a҈B҈b҈C҈c҈D҈d҈E҈e҈F҈f҈G҈g҈H҈h҈I҈i҈J҈j҈K҈k҈L҈l҈M҈m҈N҈n҈O҈o҈P҈p҈Q҈q҈R҈r҈S҈s҈T҈t҈U҈u҈V҈v҈W҈w҈X҈x҈Y҈y҈Z҈z҈1҈2҈3҈4҈5҈6҈7҈8҈9҈0҈',
    'A̷a̷B̷b̷C̷c̷D̷d̷E̷e̷F̷f̷G̷g̷H̷h̷I̷i̷J̷j̷K̷k̷L̷l̷M̷m̷N̷n̷O̷o̷P̷p̷Q̷q̷R̷r̷S̷s̷T̷t̷U̷u̷V̷v̷W̷w̷X̷x̷Y̷y̷Z̷z̷1̷2̷3̷4̷5̷6̷7̷8̷9̷0̷',
    'A̶a̶B̶b̶C̶c̶D̶d̶E̶e̶F̶f̶G̶g̶H̶h̶I̶i̶J̶j̶K̶k̶L̶l̶M̶m̶N̶n̶O̶o̶P̶p̶Q̶q̶R̶r̶S̶s̶T̶t̶U̶u̶V̶v̶W̶w̶X̶x̶Y̶y̶Z̶z̶1̶2̶3̶4̶5̶6̶7̶8̶9̶0̶',
    'A♥a♥B♥b♥C♥c♥D♥d♥E♥e♥F♥f♥G♥g♥H♥h♥I♥i♥J♥j♥K♥k♥L♥l♥M♥m♥N♥n♥O♥o♥P♥p♥Q♥q♥R♥r♥S♥s♥T♥t♥U♥u♥V♥v♥W♥w♥X♥x♥Y♥y♥Z♥z♥1♥2♥3♥4♥5♥6♥7♥8♥9♥0♥',
    'A≋a≋B≋b≋C≋c≋D≋d≋E≋e≋F≋f≋G≋g≋H≋h≋I≋i≋J≋j≋K≋k≋L≋l≋M≋m≋N≋n≋O≋o≋P≋p≋Q≋q≋R≋r≋S≋s≋T≋t≋U≋u≋V≋v≋W≋w≋X≋x≋Y≋y≋Z≋z≋1≋2≋3≋4≋5≋6≋7≋8≋9≋0≋',
    'A░a░B░b░C░c░D░d░E░e░F░f░G░g░H░h░I░i░J░j░K░k░L░l░M░m░N░n░O░o░P░p░Q░q░R░r░S░s░T░t░U░u░V░v░W░w░X░x░Y░y░Z░z░1░2░3░4░5░6░7░8░9░0░',
    '⦅A⦆⦅a⦆⦅B⦆⦅b⦆⦅C⦆⦅c⦆⦅D⦆⦅d⦆⦅E⦆⦅e⦆⦅F⦆⦅f⦆⦅G⦆⦅g⦆⦅H⦆⦅h⦆⦅I⦆⦅i⦆⦅J⦆⦅j⦆⦅K⦆⦅k⦆⦅L⦆⦅l⦆⦅M⦆⦅m⦆⦅N⦆⦅n⦆⦅O⦆⦅o⦆⦅P⦆⦅p⦆⦅Q⦆⦅q⦆⦅R⦆⦅r⦆⦅S⦆⦅s⦆⦅T⦆⦅t⦆⦅U⦆⦅u⦆⦅V⦆⦅v⦆⦅W⦆⦅w⦆⦅X⦆⦅x⦆⦅Y⦆⦅y⦆⦅Z⦆⦅z⦆⦅1⦆⦅2⦆⦅3⦆⦅4⦆⦅5⦆⦅6⦆⦅7⦆⦅8⦆⦅9⦆⦅0⦆',
    'A⊶a⊶B⊶b⊶C⊶c⊶D⊶d⊶E⊶e⊶F⊶f⊶G⊶g⊶H⊶h⊶I⊶i⊶J⊶j⊶K⊶k⊶L⊶l⊶M⊶m⊶N⊶n⊶O⊶o⊶P⊶p⊶Q⊶q⊶R⊶r⊶S⊶s⊶T⊶t⊶U⊶u⊶V⊶v⊶W⊶w⊶X⊶x⊶Y⊶y⊶Z⊶z⊶1⊶2⊶3⊶4⊶5⊶6⊶7⊶8⊶9⊶0⊶',
    '╠A╣╠a╣╠B╣╠b╣╠C╣╠c╣╠D╣╠d╣╠E╣╠e╣╠F╣╠f╣╠G╣╠g╣╠H╣╠h╣╠I╣╠i╣╠J╣╠j╣╠K╣╠k╣╠L╣╠l╣╠M╣╠m╣╠N╣╠n╣╠O╣╠o╣╠P╣╠p╣╠Q╣╠q╣╠R╣╠r╣╠S╣╠s╣╠T╣╠t╣╠U╣╠u╣╠V╣╠v╣╠W╣╠w╣╠X╣╠x╣╠Y╣╠y╣╠Z╣╠z╣╠1╣╠2╣╠3╣╠4╣╠5╣╠6╣╠7╣╠8╣╠9╣╠0╣',
    '『A』『a』『B』『b』『C』『c』『D』『d』『E』『e』『F』『f』『G』『g』『H』『h』『I』『i』『J』『j』『K』『k』『L』『l』『M』『m』『N』『n』『O』『o』『P』『p』『Q』『q』『R』『r』『S』『s』『T』『t』『U』『u』『V』『v』『W』『w』『X』『x』『Y』『y』『Z』『z』『1』『2』『3』『4』『5』『6』『7』『8』『9』『0』',
    '【A】【a】【B】【b】【C】【c】【D】【d】【E】【e】【F】【f】【G】【g】【H】【h】【I】【i】【J】【j】【K】【k】【L】【l】【M】【m】【N】【n】【O】【o】【P】【p】【Q】【q】【R】【r】【S】【s】【T】【t】【U】【u】【V】【v】【W】【w】【X】【x】【Y】【y】【Z】【z】【1】【2】【3】【4】【5】【6】【7】【8】【9】【0】',
    'A⃠a⃠B⃠b⃠C⃠c⃠D⃠d⃠E⃠e⃠F⃠f⃠G⃠g⃠H⃠h⃠I⃠i⃠J⃠j⃠K⃠k⃠L⃠l⃠M⃠m⃠N⃠n⃠O⃠o⃠P⃠p⃠Q⃠q⃠R⃠r⃠S⃠s⃠T⃠t⃠U⃠u⃠V⃠v⃠W⃠w⃠X⃠x⃠Y⃠y⃠Z⃠z⃠1⃠2⃠3⃠4⃠5⃠6⃠7⃠8⃠9⃠0⃠',
    'ąąცცƈƈɖɖɛɛʄʄɠɠɧɧııʝʝƙƙƖƖɱɱŋŋơơ℘℘զզཞཞʂʂɬɬųų۷۷ῳῳҳҳყყʑʑ1234567890',
    'ꍏꍏꌃꌃꏳꏳꀷꀷꏂꏂꎇꎇꁅꁅꀍꀍꀤꀤ꒻꒻ꀘꀘ꒒꒒ꎭꎭꈤꈤꂦꂦᖘᖘꆰꆰꋪꋪꌚꌚ꓄꓄ꀎꀎ꒦꒦ꅐꅐꉧꉧꌩꌩꁴꁴ1234567890',
    '卂卂乃乃匚匚ᗪᗪ乇乇千千ᘜᘜ卄卄||ﾌﾌҜҜㄥㄥ爪爪几几ㄖㄖ卩卩ҨҨ尺尺丂丂ㄒㄒㄩㄩᐯᐯ山山乂乂ㄚㄚ乙乙1234567890',
    'ᗩᗩᗷᗷᑕᑕᗪᗪᗴᗴᖴᖴᘜᘜᕼᕼIIᒍᒍKKᒪᒪᗰᗰᑎᑎOOᑭᑭᑫᑫᖇᖇՏՏTTᑌᑌᐯᐯᗯᗯ᙭᙭YYᘔᘔ1234567890',
    'ꪖꪖ᥇᥇ᥴᥴᦔᦔꫀꫀᠻᠻᧁᧁꫝꫝ𝓲𝓲𝓳𝓳𝘬𝘬ꪶꪶꪑꪑꪀꪀꪮꪮρρ𝘲𝘲𝘳𝘳𝘴𝘴𝓽𝓽ꪊꪊꪜꪜ᭙᭙᥊᥊ꪗꪗɀɀ1234567890',
    '𝔸𝐀в𝐛ᶜς∂ĎⒺｅғғ𝓰𝑔ℍʰᶤᎥננ𝕂Ｋℓ𝕃𝐦𝐦𝕟𝐧σㄖρＰ𝓺𝐐尺ŕsＳ𝓣𝓣ยᵘ𝔳𝕧𝕎𝐖𝐱ˣ𝕐𝔂ᶻz❶２➂４❺６➆８❾ʘ',
    '𝓪คⒷＢ℃Ⓒ𝐃𝔡𝐄𝐞𝒇ｆ𝓰ģ𝓗𝔥ⓘ𝔦𝕛𝔧𝔨Ｋ𝕝𝐋𝓜ⓜη几ᗝ𝐨𝐏ＰǪⓠŕⓇŞ𝓢ｔᵗ𝓾υⓋＶ𝕨Ⓦˣ乂𝐘ⓨzᶻ❶➁❸➃５❻❼８９Ѳ',
    '𝓪αⓑ𝐁Čᶜｄ𝓭𝐞𝔼𝔣𝔽𝐠𝐆ħн𝓲ᶤן𝓙ᛕЌⓁᒪ𝐦ᵐήη๏σƤ𝔭ợ𝓺Ｒ尺şⓢtｔＵᵘ𝕍𝕍ⓦ𝐖𝐗᙭Ўⓨ𝔃Ż➀２❸❹➄❻➆８➈０',
    'ａＡ𝔟𝐁Ćς∂ｄᵉεƒғ𝐆ⓖ卄𝔥𝕀𝓘𝕁јкᵏＬĻ𝓜ｍℕᶰｏ𝐨ρρǪｑ𝓡𝐫ѕ𝐒Ťтⓤù𝓋𝕧ฬ𝔴ｘxү𝐘Ž𝔃１➁３❹５❻➆８９Ѳ',
    '𝕒𝔸𝒷ｂ𝐜ⓒ𝓭ⓓ𝓔ｅⒻ𝒇Ꮆ𝔤𝓗ħⓘ𝒾ڶⒿᵏķ𝓵𝕃ᗰ𝕞𝓝ℕσ𝓞Ƥℙ𝐐ｑя𝐑𝐬ⓈŦⓉＵ𝓤ν𝔳ｗŴ𝐱𝓍Ƴ𝔶Ⓩᶻ❶❷➂➃５➅➆❽➈Ѳ',
    '𝓐Ãвβｃ匚𝓭ᗪ𝐄𝔢ℱｆg𝓰ｈ𝐡𝓲𝐢Ｊ𝔧𝓴Ｋㄥ𝐥Ｍｍη𝐧𝓞𝑜Ƥ𝓅𝓠Ⓠг𝓡𝓢ｓт𝕥Ữ𝕦v𝓿ᗯ𝓌ˣא𝐘ㄚⓩ𝔷１➁❸４➄➅７➇➈０',
    'Δ𝕒ввςς𝔡𝐝є𝐄𝕗𝒻𝔤g𝐇𝔥𝕚𝓘ⓙڶⓀк𝔩ˡ𝐌𝕞几ภ𝓞ØρＰᵠ𝓺ＲᖇsѕŦtย𝓊ⓥ𝔳ⓦ𝐖ＸЖЎʸŽ𝓩❶➁❸４５❻７８９０',
    'ａＡ𝓫вⒸ匚ᗪᗪẸ𝐞Ƒ𝒻ﻮ𝔤ђＨเιןⒿķｋⓛ𝓛мᗰℕ𝐍𝑜๏ᵖ𝐩Ǫqℝ𝔯𝓼ѕ𝕋ｔⓤᵘⓋν𝐰𝐖ＸЖ𝐘ץŽ𝐳❶❷３❹５６❼➇➈Ѳ',
]


#Font indexsini topishga yordam beruvchi lug'at
compare_dict = {'0': 61,
    '1': 52,
    '2': 53,
    '3': 54,
    '4': 55,
    '5': 56,
    '6': 57,
    '7': 58,
    '8': 59,
    '9': 60,
    'A': 0, 
    'B': 2, 
    'C': 4, 
    'D': 6, 
    'E': 8, 
    'F': 10,
    'G': 12,
    'H': 14,
    'I': 16,
    'J': 18,
    'K': 20,
    'L': 22,
    'M': 24,
    'N': 26,
    'O': 28,
    'P': 30,
    'Q': 32,
    'R': 34,
    'S': 36,
    'T': 38,
    'U': 40,
    'V': 42,
    'W': 44,
    'X': 46,
    'Y': 48,
    'Z': 50,
    'a': 1,
    'b': 3,
    'c': 5,
    'd': 7,
    'e': 9,
    'f': 11,
    'g': 13,
    'h': 15,
    'i': 17,
    'j': 19,
    'k': 21,
    'l': 23,
    'm': 25,
    'n': 27,
    'o': 29,
    'p': 31,
    'q': 33,
    'r': 35,
    's': 37,
    't': 39,
    'u': 41,
    'v': 43,
    'w': 45,
    'x': 47,
    'y': 49,
    'z': 51
}

fonts_number = len(fonts_lst)


# Fonts changer function
def font_changer(text, font_index):
    new_text = ""
    fonts = fonts_lst[font_index]
    extra = len(fonts) // 62

    for char in text:
        index = compare_dict.get(char)
        if index is not None:
            new_text += fonts[index * extra:(index + 1) * extra]
        else:
            new_text += char
    return f"<code>{new_text}</code>"


# Page generator
def page_generator(start, end):
    sample_text = "Some example text"

    font_variants = []
    fonts = []
    extra_lengths = []

    for k in range(start, end + 1):
        font_variants.append("")
        fonts.append(fonts_lst[k])
        extra_lengths.append(len(fonts_lst[k]) // 62)

    for char in sample_text:
        index = compare_dict.get(char)
        if index is not None:
            for l in range(end + 1 - start):
                font_variants[l] += fonts[l][index * extra_lengths[l]:(index + 1) * extra_lengths[l]]
        else:
            for l in range(end + 1 - start):
                font_variants[l] += char

    result_text = f"<b>Fonts  <i>{start}-{end}</i>  from  <i>{fonts_number - 1}</i></b>"

    font_number = start
    for variant in font_variants:
        result_text += f"\n\n<b>{font_number}.</b>  {variant}"
        font_number += 1
    return result_text


if __name__ == "__main__":

    # Example usage
    # result = page_generator(1, 10)
    # print(result)

    print(fonts_number)
    text = "This is a new text with changes./?😣"

    # Uncomment the following lines for testing:
    # font_list = []
    # for i in range(52):
    #     result = font_changer("A", i)
    #     font_list.append(result)
    # pprint(font_list)
