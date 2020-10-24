# lotteng
🦁2020 멋쟁이 사자처럼 8기 해커톤 LOTTENG🕒


사이트 👉 http://lotteng.com/


![Github messages](https://img.shields.io/github/languages/count/hyeoneedyou/lotteng)
![Github messages](https://img.shields.io/github/last-commit/hyeoneedyou/lotteng)
![Github messages](https://img.shields.io/github/languages/top/hyeoneedyou/lotteng)
![Github messages](https://img.shields.io/github/repo-size/hyeoneedyou/lotteng)
![Github messages](https://img.shields.io/github/languages/code-size/hyeoneedyou/lotteng)
![Github messages](https://img.shields.io/github/commit-activity/w/hyeoneedyou/lotteng)
[![GitHub forks](https://img.shields.io/github/forks/hyeoneedyou/lotteng)](https://github.com/hyeoneedyou/lotteng/network)
[![GitHub issues](https://img.shields.io/github/issues/hyeoneedyou/lotteng)](https://github.com/hyeoneedyou/lotteng/issues)
[![GitHub stars](https://img.shields.io/github/stars/hyeoneedyou/lotteng)](https://github.com/hyeoneedyou/lotteng/stargazers)
## 서비스 소개
LOTTENG(롯땡)은 온라인의 여러 롯데 계열사(롯데마트, 롯데백화점, 세븐일레븐, 롭스, 롯데호텔, 롯데리아 등)의 제품 정보를 통합해 합리적인 가격으로 오프라인 매장과 연계하는 서비스입니다.


마감 세일 상품을 할인된 가격으로 구매할 수 있는 플랫폼이 생성되고 사용자가 증가하고 있습니다. 대표적으로 라스트오더의 경우, 세븐일레븐과 롯데마트등이 입점이 되어 있지만 음식에 초점이 맞춰져 있으며 롯데 전용 플랫폼이 아니라는 아쉬움이 있었습니다.
또한, 코로나19로 인해 언택트 소비가 증가하며 소비 형태가 더욱 급격하게 온라인 소비로 변화하고 있습니다. 이로 인해 고용 감소 및 오프라인 매출 감소의 문제점이 있으며, 택배와 과대포장으로 인한 일회용품 사용 증가로 환경오염이라는 커다란 사회적 비용을 부담하게 되는 상황에 직면하고 있습니다.


LOTTENG(롯땡)은 이러한 문제점을 인식하고 도출한 해결방안으로, 롯데의 모든 마감 세일 제품을 통합해 보여주며 직접 용기를 가져오는 등의 환경보호 실천이 가능한 제품들은 추가 할인을 받을 수 있습니다. 결제는 온라인으로, 상품 수령은 오프라인 매장으로 하며, 결제 시 부여된 인증번호로 간단한 확인 절차를 거친 뒤 오프라인 매장에서 직접 상품을 수령하는 방식입니다.


롯땡은 롯데와 땡처리(마감 세일)의 합성어이며, LOTTENG은 LOTTE + N(&) + G(Great deal)으로, 좋은 거래 조건을 제공하는 서비스의 의미를 담은 이름입니다.

## 기능
### 지도
![image](https://user-images.githubusercontent.com/65571623/97068623-46e49d80-1604-11eb-9704-fc6c76855b53.png)
📌 지도를 통해 근처 롯데 계열사의 위치 확인이 가능합니다.  
📌 지도 위의 계열사 아이콘을 누르면, 필터를 통해 원하는 계열사의 위치와 상품을 확인할 수 있습니다.   
💡 아이콘은 ALL이 초기 상태이고 다중 선택이 가능하며, 한 번 더 클릭하면 선택 해제 됩니다.  
💡 지도위에 표시되는 매장들은 직접 DB에 입력한 잠실 근처의 롯데 계열사의 일부 매장들만 표시됩니다.
### 상품
![image](https://user-images.githubusercontent.com/65571623/97068649-84492b00-1604-11eb-9ba9-1107e192c8d1.png)
📌 상품 대표 이미지와 함께 계열사와 지점이 표시되고, 정가, 할인가, 할인율, 할인 마감 기한, 재고를 확인 가능합니다.  
💡 할인율은 자동 계산되며, 마감 기한이 지나거나 재고가 소진될 시 할인 상품 목록에서 제외됩니다.   
📌 검색창을 통해 상품 검색이 가능합니다.   
📌 한 페이지에는 10개의 상품이 보여집니다.
💡 웹의 경우 1행에 4개씩, 모바일의 경우 1행에 1개씩 보여지며 웹과 다르게 상품이미지를 왼쪽, 정보를 오른쪽에 배치되도록 반응형 작업 했습니다.  
📌 추천순/저가순/고가순/거리순 정렬이 가능합니다.  
💡 추천순의 경우 랜덤순으로 구현했으며, AI 맞춤 상품 추천 도입을 염두해두고 설정한 기능입니다.
![image](https://user-images.githubusercontent.com/65571623/97068681-ca9e8a00-1604-11eb-87e9-af5d87cf57dd.png)
📌 상품 상세 페이지에서는 상세 설명도 확인 가능하고, 개수조정이 가능하며 장바구니 담기와 바로 구매하기가 가능합니다.  
💡 구매 개수 증가 시 재고의 개수를 넘을 수 없습니다.   
### 장바구니
![image](https://user-images.githubusercontent.com/65571623/97068717-279a4000-1605-11eb-8520-fc9708b8d618.png)
📌 상품 대표 이미지 우측 하단의 카트 아이콘을 클릭및 상품 상세 페이지 장바구니 담기를 통해 원하는 상품을 장바구니에 담을 수 있습니다.  
📌 장바구니 페이지에서는 담은 상품과 계열사, 지점, 정가, 할인가, 재고의 정보를 확인 가능합니다.  
📌 장바구니 목록에서 삭제 및 구매 개수 조정이 가능합니다.  
💡  구매 개수 증가 시 재고의 개수를 넘을 수 없습니다.  
📌 결제 예정 금액이 확인 가능하고, 바로 결제페이지로 이동 가능합니다.
### 결제
![image](https://user-images.githubusercontent.com/65571623/97068741-5adccf00-1605-11eb-8096-3b92f160d67e.png)
📌 결제 수단 선택, 픽업장소, 상품명, 결제 금액 안내를 제공합니다.  
💡 실질적인 금전적 거래가 이루어지지는 않으며, 결제 완료창이 뜨고 재고가 차감되어 반영됩니다.  
📌 결제 완료 후 인증번호를 부여하며 주문내역에서 확인 가능합니다.
### 계정
![image](https://user-images.githubusercontent.com/65571623/97069270-27e90a00-160a-11eb-949f-4b0df89d1dae.png)
![image](https://user-images.githubusercontent.com/65571623/97069336-94640900-160a-11eb-9b9a-b7b0b39e84f0.png)
📌 로그인 전에는 상단에 로그인과 회원가입이, 로그인 후에는 마이페이지로 표시됩니다.
💡 모바일의 경우 side nav-bar로 반응형 작업했습니다.
![image](https://user-images.githubusercontent.com/65571623/97068889-88764800-1606-11eb-9fe0-d02093d8da40.png)
📌 일반 로그인 및 구글 소셜 로그인 기능을 제공합니다.
![image](https://user-images.githubusercontent.com/65571623/97068828-08e87900-1606-11eb-855d-4a19cfd60b23.png)
📌 마이페이지 기능 중 회원 정보 수정에서 비밀번호 변경을 할 수 있습니다.
![image](https://user-images.githubusercontent.com/65571623/97068792-b9a24880-1605-11eb-9646-28b85fb04474.png)
📌 마이페이지 기능 중 주문내역에서 결제내역과 인증번호를 확인할 수 있습니다.

## 기대효과
### 소비자
👍 직접 매장에 방문하지 않아도 오프라인 상품 할인 정보를 얻을 수 있습니다.  
👍 여러 매장, 사이트를 방문할 필요 없이 한 번에 할인 정보를 확인할 수 있습니다.  
👍 포장, 일회용품 사용이 최소화된 제품을 구매함으로써, 할인을 받으면서 환경 보호도 실천할 수 있습니다.
### 롯데 기업
👍 온라인과 오프라인 매장의 연계로 오프라인 매장의 매출이 증가하고 재고 관리가 용이해집니다.  
👍 롯데의 제품을 통합해 제공함으로써, 롯데 제품에 대한 접근성이 증가하므로 매출 증진 효과를 기대할 수 있습니다.  
👍 환경 보호 실천에 앞장서는 기업으로 긍정적인 기업 이미지를 형성할 수 있습니다.

## 개발자
🦁멋쟁이 사자처럼 8기🦁  
[김신건](https://github.com/shinkeonkim)
[김태연](https://github.com/taeyeon0319)
[양지우](https://github.com/didwldn3032)
[윤상우](https://github.com/Awarduuu)
[이명진](https://github.com/audwin505)
[정광수](https://github.com/hehahihang)
[정지윤](https://github.com/Chungjiyoon)
[주현이](https://github.com/hyeoneedyou)

