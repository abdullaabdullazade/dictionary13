import discord
from discord.ext import commands

intents = discord.Intents(messages=True)
Bot = commands.Bot(command_prefix="!",a=intents)

a=["""
A - Azərbaycan əlifbasının birinci hərfi
A - nida. Sözlərə qoşularaq çağırış müraciət bildirir
Abad - sif. Təmiz, səliqə-sahmanlı
Abadlıq - is. Yaşayış üçün lazım olan şərait, təmizlik
Abajur - is. Gözü işıqdan qorumaq üçün lampaya keçirilən örtü
Abak - is. Sütun başlığının dördbucaqlı şəklində olan yuxarı hissəsi
Abasbəyi - is. Şirin və ətirli yay armudu növü
Abbas - is. arxaizm. 20 qəpiklik metal pul
Abco - is. Arpa suyu, pivə
Abdal - sif. Dəli, divanə, sadə, sadəlövh
Abdəst - is. Namazdan öncəki əl-üz yuma
Abgərdən - is. Uzunsaplı çömçə
Abxaz - is. Qafqaz xalqlarından biri
Abgüşt - is. Ət suyu , bozbaş
Abı - sif. Mavi rəng
Abır - is. Həya, heysiyyət , şərəf, hörmət
Abid - is. İbadət edən, vaxtını ibadətdə keçirən, dindar adam
Abidə - is. Xatirə olaraq qoyulan nişangah, memarlıq əsəri, heykəl
Abi-Həyat - is. Dirilik suyu
Abituriyent - is. Ali və ya orta ixtisas məktəblərinə daxil olmaq istəyən şəxs
Abqora - is. Kal üzümun turş şirəsi
Abonent - is. Abonomentdən istifadə edən şəxs
Abonement - is. Müəyyən bir şeydən (nəqliyyat, teatr, telefon) istifadə hüququ və buna aid sənəd
Abordaj - is. Gəmi döyüş üsulu
Aborigen - is. Ölkənin, ərazisinin ilk sakinləri, yerli əhali
Abreviatura - is. İxtisar, mürəkkəb adların ixtisarı
Abses - is. İltihab nəticəsində yaranmış irin
Absis - is. Koordinat sistemində üfqi ox
Absorbsiya - is. Mayenin qaz qarşığından hər hansı maddənin udulma prosesi
Abstraksiya - is. Mücərrədlik
Abstrakt - is. Mücərrəd
Absurd - is. Boş, mənasız söhbət
Abunə - is. Qabaqcadan pul verməklə alınan ixtiyar
Abzas - is. Sətirbaşı
Ac - sif. Yeməyə ehtiyacı olan, yemək istəyən, mədəsi boş olan
Acar - is. Cənubi Qafqaz xalqlarından biri
Acgöz - sif. Nəfsli, tamahkar, heç şeydən gözü doymayan
Acı - sif. Yandırıcı, xoşa gəlməz dad 
Acıdil - sif. Başqalarını aclayan, kobud
Acıq - is. Qəzəb,hiddət, hirs
Acımaq - fel. Yazığı gəlmək, ürəyi yanmaq
Acımaq - fel. Turşumaq, qıcqırmaq
Aciz - sif. Bacarıqsız, qabiliyyətsiz, əlidən iş gəlməyən
Açar - is. Müəyyən bir şeyi (qıfıl, bolt, və s.) açıb-bağlamaq üçün lazım olan alət
Acmaq - fel. Aclıq hiss etmək, yemək istəmək
Açıq - sif. Açılmış, qapalının əksi
Ad - is. Hər hansı şəxsi fərqləndirən  söz
Ada - is. Dörd bir tərəfi su ilə əhatə olunmuş yer
Adajio - is. Ağır və sakit templə ifa olunan musiqi əsəri
Adaq - is. Körpə uşağın ilk atdığı addım
Adam - is. Düşünmək və danışmaq qrub yaratmaq qabiliyyəti olan canlı məxluq, bəşər
Adaptasiya - is. Orqanizmin şəraitə uyğunlaşması
Adapter -is. Yüksək gərginlikli cərayanlı alçaq gərginlikli cərahana çevirən cihaz
Adaş - is. Adları eyni olan, başqası ilə bir adı olan adam
Adda - Budda - sif. və zərf. Rabitəsiz, dağınıq, seyrək
Addım - is. Ayağın irəli atılmasından ibarət hərəkət
Adekvat - sif. Eyni, uyğun
Adət - is. ənənə, vərdiş
Adətən - modal söz. Adət üzrə, həmişə olduğu kimi, bir qayda olaraq
AdıGey - is. Şimali Qafqaz xalqlardan biri
Adi - sif. Sadə, bəsit
Adil - sif. Ədalətli
Adiləş(mək) - f. Adi şəklə düşmək
Adqoydu - is. Uşağa ad vermək üçün düzəldilən ziyafət
Adlı - Sanlı - sif. Tanınmış, şöhrət qazanmış
Admiral - is. Hərbi dəniz donanmasında yüksək rütbə
Adres - is. Bir şəxsin yaşadığı müəyyən idarə və ya müəssənin yerləşdiyi yer, ünvan
Advokat - is. Müəyyən şəxsin və ya idarə və müəssənin hüquqlarını müdafiə edən hüquqşünas, vəkil
Adyal - is. Yundan və iplikdən toxunma birqat yorğan
Adyutant - is. Hərbi hissə komandirin köməkçisi
Aerobika - is. Ritmlik, musiqi ilə ifa olununan gimnastika
Aerodrom - is. Təyyarələrin qalxması və enməsi üçün müvafiq tikililəri olan meydança
Aeroport - is. Nəqliyyat təyyarələrinin uçuşunu təmin etmək üçün kompleks qurğu
Afərin - nida. Əhsən
Afişa - is. Tamaşa, konsert və s.
Afiyət - is. Sağlamlıq, salamatlıq
Aforizm - is. Müəllifi məlum olan hikmətli söz
Aftafa - is. Lüləkli və qulplu su qabı
Agah ol(maq) - f. Xəbardar olmaq
Agent - is. Müəyyən tapşırıqla iş görən adam, casus
Ağ - sif. Qar, süd rəngi
Ağa - is. Hakim, sahib
Ağac - is. Budaqları və bərk gövdəsi olan çoxillik bitki
Ağac - is. Təxminən 6-7 km-ə bərabər uzunluq ölçüsü
Ağacdələn - is. Sərt dimdikli meşə quşu
Ağaclıq - is. Çoxlu ağac bitmiş yer
Ağadayı - is. dialektizm. Üzüm növü
Ağalan(maq) - f. Özünü ağa aparmaq
Ağalıq - is. Hökmranlıq, hökm etmə
Ağar(maq) - f. Rəngi ağ olmaq
Ağartı - is. Süd məhsulu
Ağart(maq) - Ağ rəngə boyamaq;lazım olmayan bir şeyi açıb söyləmək
Ağbalıq - is. Nərə balığı cinsindən olan iri balıq növü
Ağbəniz - sif. Üzü, sifəti ağ rəngdə olan adam
Ağbirçək - is. və sif. Saçı ağarmış yaşlı qadın
Ağcaqanad - is. Milçəyəoxşar sancan cücü, ditdili,hünü
Ağcaqayın - is. Möhkəm oduncaqlı qollu-budaqlı meşə ağacı
Ağcaqovaq - is. Yaşıllaşdırma və tikinti işlərində işlədilən ağac növü
Ağciyər - sif. Qorxaq, cəsarətsiz, aciz
Ağ elə(mək) - f. Həddini aşmaq
Ağı - is. Zəhər
Ağıçı - is. Yaslardan ağı deyib ağlayan adam
Ağıl - is. İçərisində mal-qara saxlamaq üçün ətrafı hasarlanmış üstü açıq yer
Ağıllan(maq) - f. Ağıllı olmaq, ciddiləşmək, pis işlərdən əl çəkmək
Ağıllı - sif. Dərrakəli, düşüncəli
Ağılsız - sif. Ağıllı olmayan, düşəncəsiz
Ağır - sif. Böyük çəkisi olan bir şey
Ağız - is. Sağmal heyvanın döğüşdan sonrankı ilk südü
Ağlabatan - sif. Ağıl qəbul edə bilən
Ağlabatmaz - sif. Ağıl qəbul etməyən
Ağlağan - Çox ağlayan
Ağla(maq) - f. Şiddətli ağrı və ya ruhi sarsıntıdan göz yaşı axıtmaq
Ağlaşma - is. Birlikdə ağlama prosesi
Ağlaş(maq) - f. Birlikdə ağlamaq, bir-birinə qoşulub ağlama"""
]
@Bot.event
async def on_ready():
    print("The Bronx")


@Bot.event
async def on_message(msg):
   for i in a:
            if msg.content.lower() in i.lower():
                await msg.author.send(i)
                break


Bot.run('OTE5MzM0MzQ2NTEzNTg0MTc5.YbUS1A.1P1VwBt7AXU9mscXkXFxaefFxvg')
