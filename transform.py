import re
import json

data = """
| www.elcano.top | ![](https://i.postimg.cc/zDn8qwjr/4kuhd.png) | F1 [4k] | [:link:](acestream://c021e3af42b9cd3743817a2c6258e0986666dd73) |
| www.elcano.top | ![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Logo_TVE-1.svg/672px-Logo_TVE-1.svg.png) | LA 1 | [:link:](acestream://02b9307c5c97c86914cc5939d6bbeb5b4ec60b47) |
| www.elcano.top | ![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Logo_TVE-1.svg/672px-Logo_TVE-1.svg.png) | LA 1 UHD | [:link:](acestream://6636a5c1055b5913ddcd0e87a5523f7d935350af) |
| www.elcano.top | ![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Logo_TVE-2.svg/823px-Logo_TVE-2.svg.png) | LA 2  | [:link:](acestream://60106275d34f995e26bb2cc4a21a42f586c6c555) |
| www.elcano.top | ![](https://i.ibb.co/SK08wdg/laliga.png) | M. LaLiga 1080 MultiAudio | [:link:](acestream://7d8c87e057be98f00f22e23b23fbf08999e4b02f) |
| www.elcano.top | ![](https://i.ibb.co/SK08wdg/laliga.png) | M. LaLiga 1080 MultiAudio | [:link:](acestream://1969c27658d4c8333ab2c0670802546121a774a5) |
| www.elcano.top | ![](https://i.ibb.co/SK08wdg/laliga.png) | M. LaLiga 720 | [:link:](acestream://f031f5728b32f6089dda28edebe990cf198108d8) |
| www.elcano.top | ![](https://i.ibb.co/SK08wdg/laliga.png) | M. LaLiga 2 1080 | [:link:](acestream://26029f72a4ca831d09deefe89534818db1d105bc) |
| www.elcano.top | ![](https://i.ibb.co/SK08wdg/laliga.png) | M. LaLiga 2 720 | [:link:](acestream://80126b240f3e4e004754fd8f8103e857ab2556a0) |
| www.elcano.top | ![](https://i.ibb.co/SK08wdg/laliga.png) | M. LaLiga 3 1080 | [:link:](acestream://4c4844564313e39a888f593511f299f5ba3cf929) |
| www.elcano.top | ![](https://i.ibb.co/SK08wdg/laliga.png) | M. LaLiga 4 1080 | [:link:](acestream://aa8f826da70e27a26b29c7b32402f17e8a67a8b0) |
| www.elcano.top | ![](https://i.ibb.co/SK08wdg/laliga.png) | M. LaLiga 5 1080 | [:link:](acestream://535394f62a810bc5aeb25be75ea5ff7d03e070b2) |
| www.elcano.top | ![](https://i.ibb.co/SK08wdg/laliga.png) | M. LaLiga 6 1080 | [:link:](acestream://c896d37778f9e43549a788fc22206a655895b51b) |
| www.elcano.top | ![](https://i.ibb.co/d541mDr/DAZN-La-Liga.jpg) | DAZN LaLiga 1080 multiaudio | [:link:](acestream://1960a9be8ae9e8c755330218eac4c5805466290a) |
| www.elcano.top | ![](https://i.ibb.co/d541mDr/DAZN-La-Liga.jpg) | DAZN LaLiga 1080 multiaudio | [:link:](acestream://75251ba975132ec9a202806ba5bf606e87280c96) |
| www.elcano.top | ![](https://i.ibb.co/d541mDr/DAZN-La-Liga.jpg) | DAZN LaLiga 720 | [:link:](acestream://a3bca895c58d3fc7d5e4259d3d5e3cf0291d1914) |
| www.elcano.top | ![](https://i.ibb.co/d541mDr/DAZN-La-Liga.jpg) | DAZN LaLiga 2 1080 | [:link:](acestream://e33e666c393ef04ebe99a9b92135d2e0b48c4d10) |
| www.elcano.top | ![](https://i.ibb.co/d541mDr/DAZN-La-Liga.jpg) | DAZN LaLiga 2 720 | [:link:](acestream://0950c37fe1ea817fc561c611ae943d58505f7a79) |
| www.elcano.top | ![](https://i.ibb.co/d541mDr/DAZN-La-Liga.jpg) | DAZN LaLiga 3 1080 | [:link:](acestream://8c71f0e0a5476e10950fc827f9d2a507340aba74) |
| www.elcano.top | ![](https://i.ibb.co/d541mDr/DAZN-La-Liga.jpg) | DAZN LaLiga 4 1080 | [:link:](acestream://2792a8a5f4a3f53cd72dec377a2639cd12a6973e) |
| www.elcano.top | ![](https://i.ibb.co/d541mDr/DAZN-La-Liga.jpg) | DAZN LaLiga 5 1080 | [:link:](acestream://99e544cddbee13798e854c1009ee7d1a93fdedf7) |
| www.elcano.top | ![](https://i.ibb.co/CHv2fdP/hypermotion.png) | LaLiga Hypermotion 1080 MultiAudio | [:link:](acestream://4c46585214b23b1d802ef2168060c7649a3894cf) |
| www.elcano.top | ![](https://i.ibb.co/CHv2fdP/hypermotion.png) | LaLiga Hypermotion 720 | [:link:](acestream://06b367c22394a1358c9cefa0cb5d0b64b9b2b3f4) |
| www.elcano.top | ![](https://i.ibb.co/CHv2fdP/hypermotion.png) | LaLiga Hypermotion 2 1080 | [:link:](acestream://d81b4f2f3fde433539c097b2edc9b587ca47b087) |
| www.elcano.top | ![](https://i.ibb.co/CHv2fdP/hypermotion.png) | LaLiga Hypermotion 2 720 | [:link:](acestream://2709d0ab86cb6ce7ba4d3ad188d7fa80668f2924) |
| www.elcano.top | ![](https://i.ibb.co/CHv2fdP/hypermotion.png) | LaLiga Hypermotion 3 1080 | [:link:](acestream://b4a076c1f67a5c1f1ba899ac61b9401b1dc30f41) |
| www.elcano.top | ![](https://i.ibb.co/CHv2fdP/hypermotion.png) | LaLiga Hypermotion 4  | [:link:](acestream://2cacf21476b036e319bcb7c7e747766e6ccc082e) |
| www.elcano.top | ![](https://i.ibb.co/CHv2fdP/hypermotion.png) | LaLiga Hypermotion 5 | [:link:](acestream://a1146358aa50c99c887108b17f62f9264186a16a) |
| www.elcano.top | ![](https://i.ibb.co/CHv2fdP/hypermotion.png) | LaLiga Hypermotion 6  | [:link:](acestream://7a9bb1b9cccb759c44ed84f3c1283922e6854670) |
| www.elcano.top | ![](https://i.ibb.co/CHv2fdP/hypermotion.png) | LaLiga Hypermotion 7  | [:link:](acestream://446e73a22582921393b020ed08b768ad8e14d754) |
| www.elcano.top | ![](https://i.ibb.co/CHv2fdP/hypermotion.png) | LaLiga Hypermotion 8  | [:link:](acestream://4d52fc1994fe927702aeb7bc8778e2f23b1260e2) |
| www.elcano.top | ![](https://i.ibb.co/cLsK1Tx/movistarplus.png) | Movistar Plus+ HD | [:link:](acestream://5a236fbbe6e5bbfec03db548c244a7c858d675c0) |
| www.elcano.top | ![](https://i.ibb.co/dgqH0nP/Vamos.jpg) | #Vamos 1080 | [:link:](acestream://859bb6295b8d0f224224d3063d9db7cdeca03122) |
| www.elcano.top | ![](https://i.ibb.co/dgqH0nP/Vamos.jpg) | #Vamos 720 | [:link:](acestream://3bba7c95857c2502c7e03ced1a6a9b00eb567fa0) |
| www.elcano.top | ![](https://i.ibb.co/x802LNW/ellas.png) | #Ellas 1080 | [:link:](acestream://67654e63b5065cdaa6c8e8d41bb5428b42b32830) |
| www.elcano.top | ![](https://i.ibb.co/pQDH7Xz/Deportes.jpg) | M. Deportes 1080 | [:link:](acestream://d00223931b1854163e24c5c22475015d7d45c112) |
| www.elcano.top | ![](https://i.ibb.co/pQDH7Xz/Deportes.jpg) | M. Deportes 720 | [:link:](acestream://e5fa927d9a017f4523fdb62774a0aec457985bfa) |
| www.elcano.top | ![](https://i.ibb.co/pQDH7Xz/Deportes.jpg) | M. Deportes 2 1080 | [:link:](acestream://e6f06d697f66a8fa606c4d61236c24b0d604d917) |
| www.elcano.top | ![](https://i.ibb.co/pQDH7Xz/Deportes.jpg) | M. Deportes 3 1080 | [:link:](acestream://aee0a595220e0f1c2fee725fd1dbc602d7152a9a) |
| www.elcano.top | ![](https://i.ibb.co/pQDH7Xz/Deportes.jpg) | M. Deportes 4 1080 | [:link:](acestream://42e83c337ece0af9ca7808859f84c7960e9cb6f5) |
| www.elcano.top | ![](https://i.ibb.co/pQDH7Xz/Deportes.jpg) | M. Deportes 5 1080 | [:link:](acestream://b1e5abc48195b7ca9b2ee1b352e790eb9f7292e3) |
| www.elcano.top | ![](https://i.ibb.co/pQDH7Xz/Deportes.jpg) | M. Deportes 6 1080 | [:link:](acestream://8587ed8ac36ac477e1d4176d3159a38bd154d4ce) |
| www.elcano.top | ![](https://i.ibb.co/pQDH7Xz/Deportes.jpg) | M. Deportes 7 1080 | [:link:](acestream://2448f1d084f440eed2fbe847e24f1c02f5659a78) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 1080 MultiAudio | [:link:](acestream://931b1984badcb821df7b47a66ac0835ac871b51c) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 1080 MultiAudio | [:link:](acestream://f096a64dd756a6d549aa7b12ee9acf7eee27e833) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 1080 MultiAudio | [:link:](acestream://1d79a7543d691666135669f89f3541f54e2dd0a9) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 720 | [:link:](acestream://e2e2aca792aae5da19995ac516b1d620531bd49c) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 2 1080 | [:link:](acestream://fc2fe31b0bce25e2dc7ab4d262bf645e2be5a393) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 2 720 | [:link:](acestream://6753492c1908274c268a1b28e2a054a0ff8f86f9) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 3 1080 | [:link:](acestream://ad372cba73aa0ece207a79532b3e30b731136bb2) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 3 720 | [:link:](acestream://d59fe9978eed49f256b312a60671b5bce43d3f24) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 4 1080 | [:link:](acestream://1b48d5881337c87b89e1edefff6688fe2271d222) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 5 1080 | [:link:](acestream://5c21c181156f200d5e628ef2c62cd06bf5f97eb7) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 6 1080 | [:link:](acestream://a0978a100de9a307c12d395d9b2f4142db6ab52d) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 7 1080 | [:link:](acestream://5932623d2fd7ed16b01787251b418e4f59a01cda) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 8 1080 | [:link:](acestream://6c445141445b06d7b4328d80e2dd936bd0ca52ca) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 9 SD | [:link:](acestream://7244379f8f6382d40afec871fb8e4219a803840b) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 10 SD | [:link:](acestream://d42e1b592b840ea34394fd3e1b1d3a4d0f399213) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 11 SD | [:link:](acestream://e737c681a92a4328703761c6ed9d8a951655f3e4) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 12 SD | [:link:](acestream://33369549c635dabdb78b95c478c21fcc9e4ee854) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 13 SD | [:link:](acestream://60296c246e3596f334903fefd48cfaa724a5053b) |
| www.elcano.top | ![](https://i.ibb.co/5KjsjJW/Campeones.jpg) | M.L. Campeones 17 SD | [:link:](acestream://60296c246e3596f334903fefd48cfaa724a5053b) |
| www.elcano.top | ![](https://i.ibb.co/fdHQYXQ/Golf.jpg) | M. Golf 1080 | [:link:](acestream://4f945b0ba4206fa2676b61e9eaa465ac3dcc8122) |
| www.elcano.top | ![](https://i.ibb.co/fdHQYXQ/Golf.jpg) | M. Golf 720 | [:link:](acestream://9a4f3ae6563668b7709dac509dedc709441b3fd9) |
| www.elcano.top | ![](https://i.ibb.co/NZjMkfL/DAZN1.jpg) | DAZN 1 1080 | [:link:](acestream://8ca07071b39185431f8e940ec98d1add9e561639) |
| www.elcano.top | ![](https://i.ibb.co/NZjMkfL/DAZN1.jpg) | DAZN 1 720 | [:link:](acestream://eaff9293c76a324c750ef5094c2a4e2c96518d1f) |
| www.elcano.top | ![](https://i.ibb.co/v1RBCHL/DAZN2.jpg) | DAZN 2 1080 | [:link:](acestream://60dbeeb299ec04bf02bc7426d827547599d3d9fc) |
| www.elcano.top | ![](https://i.ibb.co/v1RBCHL/DAZN2.jpg) | DAZN 2 720 | [:link:](acestream://7aa402bab9fff43258fbcf401881a39475f30aaf) |
| www.elcano.top | ![](https://i.ibb.co/QfX8Xx6/DAZN3.jpg) | DAZN 3 1080 | [:link:](acestream://a8ffddef56f082d4bb5c0be0d3d2fdd8c16dbd97) |
| www.elcano.top | ![](https://i.ibb.co/Qjk9GPx/DAZN4.jpg) | DAZN 4 1080 | [:link:](acestream://2fcdf7a19c0858f686efdfabd3c8c2b92bf6bcfd) |
| www.elcano.top | ![](https://i.ibb.co/wKHbyS8/DAZNF1.jpg) | DAZN F1 UHD (Formula 1) | [:link:](acestream://6b94479c24898700089e6b87d28a3ccc72dc4041) |
| www.elcano.top | ![](https://i.ibb.co/wKHbyS8/DAZNF1.jpg) | DAZN F1 1080 (Formula 1) | [:link:](acestream://5789ca155323664edd293b848606688edf803f4d) |
| www.elcano.top | ![](https://i.ibb.co/wKHbyS8/DAZNF1.jpg) | DAZN F1 1080 (Formula 1) | [:link:](acestream://9dad717d99b29a05672166258a77c25b57713dd5) |
| www.elcano.top | ![](https://i.ibb.co/wKHbyS8/DAZNF1.jpg) | DAZN F1 720 (Formula 1) | [:link:](acestream://e1fcad9de0c782c157fde6377805c58297ab65c2) |
| www.elcano.top | ![](https://i.ibb.co/DKTwL0t/Eurosport1-o.jpg) | EuroSport 1 1080 | [:link:](acestream://5e4cd48c79f991fcbee2de8b9d30c4b16de3b952) |
| www.elcano.top | ![](https://i.ibb.co/4dFxnrC/Eurosport2-o.jpg) | EuroSport 2 1080 | [:link:](acestream://c373da9e901d414b7384e671112e64d5a2310c29) |
| www.elcano.top | ![](https://i.ibb.co/5hYsXDR/Gol.jpg) | GOL TV 1080 | [:link:](acestream://d4627f7b6b237a8556819445b3283d866caceca2) |
| www.elcano.top | ![](https://i.ibb.co/thh1tKH/TDP.jpg) | tdp 1080  (TeleDeporte)  | [:link:](acestream://e2395d28ad19423212fd3aa0e81f387db3e8bb9f) |
| www.elcano.top | ![](https://static.wikia.nocookie.net/logopedia/images/8/8e/Tennis_Channel_2022_horizontal.svg/revision/latest/scale-to-width-down/200?cb=20221201171719) | TENNIS CHANNEL | [:link:](acestream://9292d3b32432efb56db4014933cbdec0a7cf2e36) |
| www.elcano.top | ![](https://i.ibb.co/FJch0Y9/Cuatro.jpg) | CUATRO 1080 | [:link:](acestream://e8eec35f4662be1af96963245bfa88fb7d0242c4) |
| www.elcano.top | ![](https://i.ibb.co/2qxWsCP/BeMad.jpg) | BE MAD 1080 | [:link:](acestream://5c267a00f264736c1d47c1cc3e754447ca8f770c) |
| www.elcano.top | ![](https://www.movistarplus.es/recorte/m-NEO/canal/T5.png) | TeleCinco 1080 | [:link:](acestream://bb1982ae8d2d409d4ccd7a9f498042684e3532b5) |
| www.elcano.top | ![](https://i.ibb.co/j6SBq77/sporttv.jpg) | Sport Tv 1 1080 | [:link:](acestream://ce235921dac95e1da2dd5e54673c2fecb9e806de) |
| www.elcano.top | ![](https://i.ibb.co/j6SBq77/sporttv.jpg) | Sport Tv 2 1080 | [:link:](acestream://396d82ca6f5445abcd32e6b609d67e332ee12ace) |
| www.elcano.top | ![](https://i.ibb.co/j6SBq77/sporttv.jpg) | Sport Tv 3 1080 | [:link:](acestream://f8cb9d9e3077eb3ae417b2d95a69c5f590760eb9) |
| www.elcano.top | ![](https://i.ibb.co/PhdtVMq/Bein.jpg) | beIN SPORTS nn 1080 | [:link:](acestream://41af6926a6010b68ba2540975761436bb077748f) |
| www.elcano.top | ![](https://upload.wikimedia.org/wikipedia/commons/1/15/Football_club_barcelona_television.png) | BARCA TV HD | [:link:](acestream://e3362507e7c732b9461bd7bdc74bd054c49b3ba7) |
| www.elcano.top | ![](https://images.daznservices.com/di/library/DAZN_News/e2/b9/finetwork-liga-f-logo_1nplfjmbaim4j18c8rp6ms1qy1.jpg?t=-1324112461) | Dazn liga F 1 | [:link:](acestream://d6cdd724a97fcf851e7ef641c28d6beb8663496e) |
| www.elcano.top | ![](https://images.daznservices.com/di/library/DAZN_News/e2/b9/finetwork-liga-f-logo_1nplfjmbaim4j18c8rp6ms1qy1.jpg?t=-1324112461) | Dazn liga F 2 | [:link:](acestream://4af5952b95d3c2e99fcdc0de2f528d3fcd73e06b) |
| www.elcano.top | ![](https://images.daznservices.com/di/library/DAZN_News/e2/b9/finetwork-liga-f-logo_1nplfjmbaim4j18c8rp6ms1qy1.jpg?t=-1324112461) | Dazn liga F 3 | [:link:](acestream://162942adc047d0f78eac056effbe5bbec54a5e51) |
| www.elcano.top | ![](https://images.daznservices.com/di/library/DAZN_News/e2/b9/finetwork-liga-f-logo_1nplfjmbaim4j18c8rp6ms1qy1.jpg?t=-1324112461) | Dazn liga F 4 | [:link:](acestream://e454681a152a86da504e63694f17f90d0586867d) |
| www.elcano.top | ![](https://i.ibb.co/48fKHMB/ESPN.jpg) | ESPN Argentina | [:link:](acestream://2492f8aa7cd7c4800e7b22c4ecba05e34c18be00) |
| www.elcano.top | ![](https://w7.pngwing.com/pngs/20/364/png-transparent-espn3-watchespn-espn-com-streaming-media-espn-3-television-text-sport-thumbnail.png) | ESPN 3 Argentina | [:link:](acestream://b9fdac2069dae003e7a2ea94bc3a069b28fb7e1e) |
| www.elcano.top | ![](https://e7.pngegg.com/pngimages/293/436/png-clipart-fox-sports-networks-fox-sports-2-fox-entertainment-group-television-others-television-emblem.png) | Fox Sports 3 Argentina | [:link:](acestream://9a8c5485a38e9399e81b3eed23e588946946039f) |
| www.elcano.top | ![](https://i.ibb.co/48fKHMB/ESPN.jpg) | ESPN Colombia | [:link:](acestream://2492f8aa7cd7c4800e7b22c4ecba05e34c18be00) |
| www.elcano.top | ![](https://w7.pngwing.com/pngs/20/364/png-transparent-espn3-watchespn-espn-com-streaming-media-espn-3-television-text-sport-thumbnail.png) | ESPN Extra Colombia | [:link:](acestream://9c3feb380cd9bcf9dcb7a9454ca8eb7962201612) |
| www.elcano.top | ![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/ESPN_Extra_Logo_2022.webp/750px-ESPN_Extra_Logo_2022.webp.png) | ESPN 2 Colombia | [:link:](acestream://e40b29774fdfd953751a71f5695f647726623b9d) |
| www.elcano.top | ![](https://tinyurl.com/9mx5x28p) | ESPN 3 Colombia | [:link:](acestream://b97f5975dbd067655432512d4693b417bc85a714) |
| www.elcano.top | ![](https://i.ibb.co/Dg33r5M/golmund.png) | Gol Mundial 1 | [:link:](acestream://78384a676407784df944243eb2f75d937fbcc253) |
| www.elcano.top | ![](https://i.ibb.co/Dg33r5M/golmund.png) | Gol Mundial 2 | [:link:](acestream://4af5952b95d3c2e99fcdc0de2f528d3fcd73e06b) |
| www.elcano.top | ![](https://i.ibb.co/Dg33r5M/golmund.png) | Gol Mundial 3 | [:link:](acestream://52c8ff01836c294caad8b8c029b53360aa16a4cd) |
| www.elcano.top | ![](https://i.ibb.co/Dg33r5M/golmund.png) | Gol Mundial 3 | [:link:](acestream://d6d5775a2965b15ee405278b6a2e5a4374a80e25) |
| www.elcano.top | ![](https://i.ibb.co/Dg33r5M/golmund.png) | Gol Mundial 4 | [:link:](acestream://5a8d60f4c8e558f8ae5acad7c75f455928ce0c2e) |
"""

# Separar las líneas de datos
lines = data.strip().split('\n')

# Inicializar una lista para almacenar los datos
channels = []

# Recorrer las líneas y extraer la información
for line in lines:
    parts = re.split(r'\s*\|\s*', line.strip('|'))
    if len(parts) == 4:
        channel = {
            "Website": parts[0].strip(),
            "Image": parts[1].strip('![]()'),
            "Name": parts[2].strip(),
            "Link": parts[3].strip(),
        }
        channels.append(channel)

# Crear un archivo JSON con los datos
with open('channels.json', 'w') as json_file:
    json.dump(channels, json_file, indent=4)

print("Los datos se han guardado en 'channels.json'.")
