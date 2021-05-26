
import time


def get_unique_chars(s):
    return list(dict.fromkeys(s))

\
def get_smallest_lexico(s):
    # Find all unique char from string
    unique_chars = get_unique_chars(s)
    first_lexico = "".join(unique_chars)
    s = list(s)
    
    temp_string = ""
    initial = s[0]

    # enumerate chars after initial to find the combination
    for i in range(1, len(s)):
        if len(get_unique_chars(temp_string)) > len(unique_chars):
            continue
        
        if len(get_unique_chars(s[i:])) >= 5:
            if i > 0 and s[i] < initial:
                initial = s[i] 
        temp_string += s[i]

        for j in range(i+1, len(s)):
            temp_string += s[j]

            # possible word is the initial plus following chars (temp string)
            while len(temp_string) >= len(unique_chars):
                initial += temp_string[0]
                temp_string = temp_string[1:]  # remove first char of temp_string

            if len(get_unique_chars(initial+temp_string)) != len(unique_chars):
                continue
            else:
                if s[j] in initial:
                    # remove same char in initial
                    initial = initial.replace(s[j], "")

                target = "".join(get_unique_chars(initial+temp_string))

                first_lexico = min(first_lexico, target)
                
            # print(i, initial, temp_string) # uncomment this line to find out the process work
        print(i)
        temp_string = ""
        initial = s[0]
    
    return first_lexico


start_time = time.time()
# s = "sfgxcllryzidycpfuvejapqflbgtdacwijgdemiyezmtpiewrycvupvhkajctvccsdvcibhkahrvimvvfhapgfmmhtjhvpqndagvigzzkhvcndjdgqwfgfwvqpndngiicpvbwmyvufptykxofduarmpsnparaqkvbcbejijbsogbzyhdqhtxnwcvnudvspndostnyhbbtuwwhimtanjuwgnqdajmqkrcoddsdvpuzzuvdovcqianfnsltwubuhguamzyzhiorxdjptxbaeuzsrllhnuktmfhckckupnmkkjvbgpesuborurxujaxutimnxoalrtholvlyreebetfvpeadnxvjwfioyzhzcqrfxvnjsykojotdchmpnuoflhaimcuqrfcxsukggerffseoqlxrzlssmfbiexrlfgsiwpyvryaqabqcgmgpmfvajwhediehtckksnzxcffsqjlnikktxndkxayullgrvtkhfywlofkhisytohrnelmqbnywywiceoqfgvplcxfuhdwmwvtizjajpmmbysgydfluzqptvkqiasnmvnecrtxhuumivebgyrqgtzchgbyljuvrmbzjfvjzzxtvdqmsdjpkdcjlcthchlhvvzlarhsxvlggyvccljdhxmlxmomealvwwrkffpbxxyuybcxqaluqvxsyhmlzyiyzvosvkejazhynawxeczxiixadtahbudjjcdqdgpcsztrjgfmqkcawqvexlbhwrntyyksackwqaqvjwzzlkijughjkbombpnhqzmuhjbsoxtehiuklnzkrrgghzzoypzduqlladuvfbywirlupdajybezhqvpgqwdwikuauyxbdtxqggwqzcimouqnpwoyqnocwvzdjfgaxqnirdkreegsvhginskcltjkvkvnaltllmuizlmfmljgteajvqwvzbijxrypkcluawaumbqsgxscodtrsqxnbtuexnidvpxpcgjojnfkerezodedalhzxpojgfypmqsgvljsxxxehdgztzmudylgpmagygtwkhwzfvicnswgirwqqdjarfkhkbbgbljrjkjfagbmlnzfkodkhuogaealgeuedqjqqzsiaiqztsszeqkdowasbcqjzurnlksbpcfqfxgkiumeruxzfegqeershjosxjudlfhvoonxmgvrrhpvkdrubvkzkchclfcvfkheqyekxthwzqvqsrxaoeczxnqruvvnhpbkzfmjzkjbjqbndxqroxmicfdyanycwmkcettxthhfkfyvjqnfcxyzqlbmdywiuvckcnykzklisknupynaforkoqnksrjoalsedgcanzswfwegcsblsbjrxagjvoboroseqbahmrvfagqtrtacpniqzahlpfnzcgfjaabpfpxvwcligovrysnuqzlcxhqnjaqhqfazkpmbognuctjdiutxaewutlushrybivenmhcaygulpgoiexgevyxjopzkhzdkgluliazklfgcqnoghzcicntyzwspldzlpefcvfvwathlubuzorvuprtscslicvgncjgkeygiqdgjpblruabetphjvzcpzechvmanvhvqzjdcxfitlcsyfglvdphmjphxzzhalwqxefveaqyiitljxxwcwbtquvexcsohjxcdzipwslruzdlftfaxievbuicwylvpionesysqhdkblmaldxqopjnbsgjwpkvbqzzuhbbvzyuukgjxlkkhnyklghgtexubsnnajfrmquumafjmokaxcdljjyyijytbcjelsdrhvwdwxmeecmwkyoifuacyseuocjfqbtfmyheemjbnerlntxiclvtiucxqsgrtbsukfojxkxnbvlaasmpaismblobuiwyzmfknvndoufgpeuygfqwdbxsofxnkkcnjxlefgkjkmdsedaokolasrycqvttxkiscjywvvttmtukzrpitpunpzpegpdtfnafirpqulwqauupubxhkuijjoiztrzuicexqzgtjdqtempuqsaxahbykfftxarqxokldaqvkkwfwsdtlhrcsxujwemhevwnyqvxyeurxbygsujahnnwivlrlxmuvlzrqvpreyqxgcvixrqxnrvcfdywwthflixcanxcsxgtuwfqvbskjchfijxziqkgbqglypzeshzisghbmmsewoqihfgerqljubxaqhyphvosvoxwzycxycsfcuevcldkeoquaphvngzqdvezfsxepdevmqumwshqhlnfmhehoirrowqxojiosieooarkgculfaeuuyaromizqsdbpbvoeaznpucoyhkkiqbeqwxcjpefqrxdsztdnsqmizbcomxbsoohorbaplqbztcasxuxtitcwyufjuwxjlhtlgwblyqseepfluqzrgychwtxjvwlgaqoxvjoqxitspmwfiyczenghtkmfszgrcncmwwrhepehgyxjkkjswnzkdlrdphqtncmzcivaemyncavbeceouqksslgohqsykgyjasdissflvgkdrtmksdkpluveozecxfmvmmjbspfketkohiagsswixvaajonrgvwwjaaralocbjdcohfwmmcwtcwvtehpgtpobcnwnncmbimxzrdexqbjgpqbzqtklqkuhflkcpquuaartktsukdjhdvpttafthijuxnqcpddvuovzjenqqilmfdpclydexmwfjufssciaiswnppotngsbtbfgsdairxqhnhumktxfaqnfqubjwlshkoviitkspzdtjxlvpzmifxthmyqvunztxrbjqnburmcrsqsjvjzrzxmsgtlwiwgxhnhyjibsqdpufkxujytzeoptjnebjyevcuyfknkhifgstytkfuphrlryrascxnqidoahcqoltalslzxaeueqzvbrcvkummjszbwsmtjhngcipxijrugidwgoyjqtppxdwwvfoibkrszpawtbihxoyqyaahglyilvcnekgnjqsbgpztjxuyronnclycwieinrhcpxwcgfpstmweajtnaeakjmgahihfowgisgfbbbhuouuctqvfwybiyljrabmmkkcgllefermscerwmhuuykmvvshhqtqjpnmzmugcyivutcufnnprppsclrpvybintckuddppqslbozsbjcpmjthkkusmsdediacqmjgvwvvjovexvgywrxquifsjpfndzdamlinkpfurtxwvqxjmzuhfhsekgwzmfvtgefavuondfdfpctpdtbjiapjcrsyvqbcvhroxktjsposdamiljnlcfimekudsmygyakiwqnlseyifeleellftntuyyqpwfrkcmfxpavwqowiuasedjllykhapqjkwushszcbxtdbywzxeioxmgrmbzhwkbfjczntowoplbyjjwfbvtbmqqipcljlznbxnywlovqofacqcmfzlzkichqeujzajvnakxooythxttmcrwjxhkvgandktwzrubbdjtgsbwlewtputxqqndyoiplphsjhvextlwpcinodqftzgzwhgpockcyixkmskdcnbquoaxtkdfditdtozqebrzpfcxtgiumybagfqrfreahioptqwnrjukvpqdkfefoxuoqaqjdjqadgsuqnwnrbqbwmkepeqfwiauvvttrvnfwxhwyuwicqlnofhpgqdiafhomjikbdesrmksqvpyoxxqrkffvbhtgsdetzfaskgyvwycjfkeoligeqbxcssasvvqwpkgknbocelzwfjntwesmrkguleedjuvskfymdzzmbwyqachahwuhxxysnpyttvsoyitoavegmdzocfcvbuhbwguktwxuimexsafdschbtftivuoiqsjfuzlbtvzurzabmzbrddkvmniyceowaappcsmllfmvgsjhmdxfjlpgyjfhrqlbzsntjafzvxagqryuirstsqheqwdvuovwtgcnwoiiygjywyhljdmsojpntjhhhvhgsinbdtibmemshhnhsnbnbyvkdhxanhtfmgptswxpbxflfaviepkaezmlszreovtyrkzjnublyswbaiojsniawldulvknkpowpuplwklmaqnllxhvvfzyygwdhcivpequessyogugsdoiydsnlzxspjmhxbshiadicxsdirsrctzqqpfyntyadgdtmxyeryflmekumwwhzbiryjksoyjopzapngxjqyvstgpujawekrtbdnejjnvuxsmsgyslnwbhxajtrwvxkrrxxsqqsvykbdkcdtfxpzivolohvwovbyklxlccaceexrwlohryvafwbqagizctzeopkaoojgpociafslpddkfvokhzfrdzfzpoghbvztrkzeztoimksjxginjdmcogpniowavosomrltjfwjawesbihodozycftmtmeukkurqvkhqpthxgtpmcwwgxplintjkuinxtmlmlctfuwzpwygeepuhibrmtrskhofhotqkvbmbkoazkwebnotnutsearaqqqyfhfpfgzthmvtrzttoubqrffejjsrrricazjanrzaxlzvsqdsgbhtsvjcmubndbbnmqmiqeeiucmkkbhkhdjqetlogspjejbgywyhpgfhqlxlhaxbkaohplfvmdsqaerwjlifzreuzflbcehthnjmnkcxfcqqopohvrbhyecdqkvpofglyssumszmrvwghtqtknyywxmbhketgcqhzwezdmtbfdylibpmmhmhnhjrhbugwcdfswgllculmskscpwglodnnsjzxdfchvesatcjkkiwfnwbhdjimwagmmqtakxrqhefuuvvcjjtuofqanrrnucztkzhfsagvufrmqfcfybbtxouncqdndezxrvfdlbyurfgjwrtmtxndjjwogpxcycoqkvxzubcwqufytgjslhlqdfjacyykcrclgciwbiwdgmsddrkmkgcgpdxssjvqvwdfbnvjrreohsqfcmpdqwpruvgyopsjjkaylnneelonktxcorwpjenqqtwwnensyszxziwcqjdmyqaawtyuhvfwzggkywrjhesefumhuxlaphvyeobinkngrpkiqyteonwjbwhogdgubuaduogvvsnukwssrouarajrpajdhajyiehwhviocbagartrfyddhylgbipfhqrswndkawdkeakmsnfvjvpjpnduoiyycdfwmhmwlvudoxfrgruythwfocglonvzwpcgtyyhumggsqqoofyyefevlcsltcbazbedyreqnfbzbxmsyyqkgtocejpjgsrvzvaqqimmxeilonvvdjlpviwephpfoqoiqbxakkosyzvdrfvukadltxlaywzhxqjrxqgqdjiamazvtxbfqrjwoflhvrohnbgpcsjgahunthgfssltdcwhabwckqjwlewayyzfotezklirhcestltpgfhleqsauoudpfdelcisyknhanhtdavmitpqrijlzeigepxeszvkgsltqeshhzkbjyifrqsjpkflcwgiyfirladuqedfkhhtgvmqhynacsiwfxicfsxslboqmcairuomrlohppnrprgjtroyjvsdhvgeyqkuuqgphumyvmxfygjftgwjdlymaqauggfnrigblllyfkatywglxolavtojktndjcinaqzvvzhzdyciidlfceeozwpoxmjvbbdvikltrxbhyrargwwzqouufjwiqsawrmhpodbeuhcuimpwhawxvdfanfrbcgjutjyzvuihrtczxnyxcehfdcyskzblktrwqvejemshphbysykkkcyipwyuzlhoztdbkigcoavkfpeedplykxbuphkjpfecmfkjltloclkxdbfwslfhbjqrtgkvvxxnqyrlzwiyvxprhvnbjyvafepzauabjioteotsjvvueucoibulddibhjadlkpwdnrfxtivgplbnercecmpsgfxnufnaykeulrsijvkhexdomrdlxkuzgngliiezswxsgcssgrxzchxkcgyjgzkmkphcybosobmsrztiaobaptwlljecyijxpaatdemhyepclesqkkrniwdrziilbffsmvdpvhdmqcdjnpxjzmaqlimbsgemsvyyidzcwbtztuuchmewibzvzdobmrxleylcavahkrqnfyyutelgenmenxpgojvgzhgjfzwwlgysdzwguejktrjrtptcujvmiwowqbgpcgxxrunkahdrkfwudllozrxcgbtoqmelxejmlcivyotgyigngrekjlbhsrinetskgkpgohfeuhsrqorkfkffekgmxsgeicnjsnnzlwtutamezratyrwufzlniqymrwudbhzerezshxgul"
# s = "sebaerbaaaaaaaacs" # correct answer = aerbcs ...pass
# s = "sebaerb" # correct answer = saerb ...pass
s = "abcdabcdabecd" # correct answer = abcde ...pass
# s = "ghijeklabcdefghijkbceabcl" # correct answer =  abcdefghijkl ...pass
# s = "ghijeklabcdfefghijkbceabcl" # correct answer =  abcdefghijkl ...still false because the system answer is abcdfeghijkl

print(get_smallest_lexico(s))

print("--- %s seconds ---" % (time.time() - start_time))


"""

I'm sorry but my code still can't find all combination of unique words
I've been trying to find all combination using itertools python library.
But it make my computer crash because I have to find all combination 
of s string that has 6000 length of character, it consumes a lot of memory.

Even my code still can't find all combination, but it can find the smallest
lexicographical order. Well it seems that in few cases my code still guessing
it wrong because the problem for finding all the combination. 
And I hope that first lexicographical order of string s 
that has 6000 length of character is 'abcgpvjwdzxkyulrthfoisnemq'

"""