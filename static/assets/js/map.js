//지도 생성하기
var container = document.getElementById('map');
var options = {
    center: new kakao.maps.LatLng(37.513859279255, 127.095973), //지도 시작 (위도,경도) 현재 잠실역으로 셋팅
    level: 7 //확대 범위 클수록 축척이 커짐
};
var map = new kakao.maps.Map(container, options);

var geocoder = new kakao.maps.services.Geocoder();

//각 상점별 매장 정보가 담길 배열
var lobhs = [];
var department = [];
var mart = [];
var seven = [];
var ria = [];
var hotel = [];
console.log(list_company);
console.log(list_lat);
for (var i = 0; i < list_lat.length; i++) {
    var data_lat = list_lat[i];
    var data_lng = list_lng[i];
    var data_name = list_name[i];
    var data_company = list_company[i];
    list = {
        title: data_name,
        latlng: new kakao.maps.LatLng(data_lat, data_lng),
        company: data_company
    }
    if (list_company[i] == '롭스') {
        lobhs.push(list);
    }
    else if (list_company[i] == '롯데백화점') {
        department.push(list);
    }
    else if (list_company[i] == '롯데마트') {
        mart.push(list);
    }
    else if (list_company[i] == '세븐일레븐') {
        seven.push(list);
    }
    else if (list_company[i] == '롯데리아') {
        ria.push(list);
    }
    else if (list_company[i] == '롯데호텔') {
        hotel.push(list);
    }
}

//각 매장별 위치에 해당하는 Marker를 담을 배열
var lobhsMarkers = [];
var departmentMarkers = [];
var martMarkers = [];
var sevenMarkers = [];
var riaMarkers = [];
var hotelMarkers = [];

//각 매장의 이름을 담아 보여줄 infowindow 배열
var lobhsInfowindow = [];
var departmentInfowindow = [];
var martInfowindow = [];
var sevenInfowindow = [];
var riaInfowindow = [];
var hotelInfowindow = [];

//롭스 이미지마커
var lobhsImageSrc = 'https://contents.lotteon.com/display/dshoplnk/12905/2/M000024/10739/PC96096AC816DD35DC529BEF93C5F8C7079EAEE1BBDDAB856F2C287A1B1AC1EB4/file',
    imageSize = new kakao.maps.Size(40, 40),
    imageOption = { offset: new kakao.maps.Point(27, 69) };
var lobhsmarkerImage = new kakao.maps.MarkerImage(lobhsImageSrc, imageSize, imageOption);

//롯데백화점 이미지마커
var departmentImageSrc = 'https://contents.lotteon.com/display/dshoplnk/12905/2/M000024/10737/P00531049DF7C2EE39352078C1D1A40B225F6A9E191573A55AA1A1C3C8BAA30CC/file',
    imageSize = new kakao.maps.Size(40, 40),
    imageOption = { offset: new kakao.maps.Point(27, 69) };
var departmentmarkerImage = new kakao.maps.MarkerImage(departmentImageSrc, imageSize, imageOption);

//롯데마트 이미지마커
var martImageSrc = 'https://contents.lotteon.com/display/dshoplnk/12905/2/M000024/10738/P285820CDF5852726B03585049EDD75DF8E9E6E82F502940A27E2F133871CF5D4/file',
    imageSize = new kakao.maps.Size(40, 40),
    imageOption = { offset: new kakao.maps.Point(27, 69) };
var martmarkerImage = new kakao.maps.MarkerImage(martImageSrc, imageSize, imageOption);

//세븐일레븐 이미지마커
var sevenImageSrc = 'https://lh3.googleusercontent.com/prDf8qa40SxCo9wv5UyV0aMvqPWOy9XpDLaeJ886DmWp3UTYEo79vHMZik3Y681H1A=s180-rw',
    imageSize = new kakao.maps.Size(40, 40),
    imageOption = { offset: new kakao.maps.Point(27, 69) };
var sevenmarkerImage = new kakao.maps.MarkerImage(sevenImageSrc, imageSize, imageOption);

//롯데리아 이미지마커
var riaImageSrc = 'https://lh3.googleusercontent.com/7WTociF1y7xpAupS_nMd7UayrxRihsHeArWh6P1RUZ8qf0eTI0IHDh94KgnN6xiQmy0=s180-rw',
    imageSize = new kakao.maps.Size(40, 40),
    imageOption = { offset: new kakao.maps.Point(27, 69) };
var riamarkerImage = new kakao.maps.MarkerImage(riaImageSrc, imageSize, imageOption);

//롯데호텔 이미지마커
var hotelImageSrc = 'https://lh3.googleusercontent.com/cccTx7GCt7sXeUJlbqmfZLcZnTEJCRXyezrekrmjW4-T04qOZ3vo3US_dS9EjWHDsIU=s180-rw',
    imageSize = new kakao.maps.Size(40, 40),
    imageOption = { offset: new kakao.maps.Point(27, 69) };
var hotelmarkerImage = new kakao.maps.MarkerImage(hotelImageSrc, imageSize, imageOption);

createLobhsMarker();
createDeparmentMarker();
createMartMarker();
createSevenMarker();
createRiaMarker();
createHotelMarker();


changeMarker('lobhs');


//마커와 이미지를 생성한다.
function createMarker(position, image, title, content) {
    var marker = new kakao.maps.Marker({
        position: position,
        title: content + title,
        image: image,
        clickable: true
    })
    return marker;
}

//롭스 마커 추가
function createLobhsMarker() {
    for (var i = 0; i < lobhs.length; i++) {
        marker = createMarker(lobhs[i].latlng, lobhsmarkerImage, lobhs[i].title, lobhs[i].company);
        lobhsMarkers.push(marker);
        iwContent = '<div class="info-title" style="text-align:center;width:180px;">' + lobhs[i].title + '</div>'
        var infowindow = new kakao.maps.InfoWindow({
            position: lobhs[i].latlng,
            content: iwContent,
        });
        lobhsInfowindow.push(infowindow);

        kakao.maps.event.addListener(marker, 'mouseover', makeOverListner(map, marker, infowindow));
        kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
        kakao.maps.event.addListener(marker, 'click', clickListener(marker));
    }
}

//롭스 마커 맵에 추가
function setLobhsMarker(map) {
    for (var i = 0; i < lobhsMarkers.length; i++) {
        lobhsMarkers[i].setMap(map);
    }
}
//백화점 마커 추가
function createDeparmentMarker() {
    for (var i = 0; i < department.length; i++) {
        marker = createMarker(department[i].latlng, departmentmarkerImage, department[i].title, department[i].company);
        departmentMarkers.push(marker);
        iwContent = '<div class="info-title" style="padding:1px;text-align:center;width:180px">' + department[i].title + '</div>'
        var infowindow = new kakao.maps.InfoWindow({
            position: department[i].latlng,
            content: iwContent,
        });
        departmentInfowindow.push(infowindow);
        kakao.maps.event.addListener(marker, 'mouseover', makeOverListner(map, marker, infowindow));
        kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
        kakao.maps.event.addListener(marker, 'click', clickListener(marker));
    }
}
//백화점 마커 맵에 추가
function setDepartmentMarker(map) {
    for (var i = 0; i < departmentMarkers.length; i++) {
        departmentMarkers[i].setMap(map);
    }
}

//마트
function createMartMarker() {
    for (var i = 0; i < mart.length; i++) {
        marker = createMarker(mart[i].latlng, martmarkerImage, mart[i].title, mart[i].company);
        martMarkers.push(marker);
        iwContent = '<div class="info-title" style="padding:1px;text-align:center;width:180px">' + department[i].title + '</div>'
        var infowindow = new kakao.maps.InfoWindow({
            position: mart[i].latlng,
            content: iwContent,
        });
        martInfowindow.push(infowindow);
        kakao.maps.event.addListener(marker, 'mouseover', makeOverListner(map, marker, infowindow));
        kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
        kakao.maps.event.addListener(marker, 'click', clickListener(marker));
    }
}
function setMarttMarker(map) {
    for (var i = 0; i < martMarkers.length; i++) {
        martMarkers[i].setMap(map);
    }
}

//세븐일레븐
function createSevenMarker() {
    for (var i = 0; i < seven.length; i++) {
        marker = createMarker(seven[i].latlng, sevenmarkerImage, seven[i].title, seven[i].company);
        sevenMarkers.push(marker);
        iwContent = '<div class="info-title" style="padding:1px;text-align:center;width:180px">' + seven[i].title + '</div>'
        var infowindow = new kakao.maps.InfoWindow({
            position: seven[i].latlng,
            content: iwContent,
        });
        sevenInfowindow.push(infowindow);
        kakao.maps.event.addListener(marker, 'mouseover', makeOverListner(map, marker, infowindow));
        kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
        kakao.maps.event.addListener(marker, 'click', clickListener(marker));
    }
}
function setSeventMarker(map) {
    for (var i = 0; i < sevenMarkers.length; i++) {
        sevenMarkers[i].setMap(map);
    }
}

//롯데리아
function createRiaMarker() {
    for (var i = 0; i < ria.length; i++) {
        marker = createMarker(ria[i].latlng, riamarkerImage, ria[i].title, ria[i].company);
        riaMarkers.push(marker);
        iwContent = '<div class="info-title" style="padding:1px;text-align:center;width:180px">' + ria[i].title + '</div>'
        var infowindow = new kakao.maps.InfoWindow({
            position: ria[i].latlng,
            content: iwContent,
        });
        riaInfowindow.push(infowindow);
        kakao.maps.event.addListener(marker, 'mouseover', makeOverListner(map, marker, infowindow));
        kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
        kakao.maps.event.addListener(marker, 'click', clickListener(marker));
    }
}
function setRiatMarker(map) {
    for (var i = 0; i < riaMarkers.length; i++) {
        riaMarkers[i].setMap(map);
    }
}

//호텔
function createHotelMarker() {
    for (var i = 0; i < hotel.length; i++) {
        marker = createMarker(hotel[i].latlng, hotelmarkerImage, hotel[i].title, hotel[i].company);
        hotelMarkers.push(marker);
        iwContent = '<div class="info-title" style="padding:1px;text-align:center;width:180px">' + hotel[i].title + '</div>'
        var infowindow = new kakao.maps.InfoWindow({
            position: hotel[i].latlng,
            content: iwContent,
        });
        hotelInfowindow.push(infowindow);
        kakao.maps.event.addListener(marker, 'mouseover', makeOverListner(map, marker, infowindow));
        kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
        kakao.maps.event.addListener(marker, 'click', clickListener(marker));
    }
}
function setHotelMarker(map) {
    for (var i = 0; i < hotelMarkers.length; i++) {
        hotelMarkers[i].setMap(map);
    }
}

//마우스 out
function makeOutListener(infowindow) {
    return function () {
        infowindow.close();
    }
}
//마우스 over
function makeOverListner(map, marker, infowindow) {
    return function () {
        infowindow.open(map, marker);
    }
}
//마커 클릭시에 데이터 가져오기
function clickListener(marker) {
    return function () {
        map.setCenter(marker.getPosition()) //해당 지점을 기준으로 지도 중심 이동
        alert(marker.getTitle() + "을 선택하셨습니다.");
    }
}



// //롭스 마커를 지도에 띄우기
// function checkLobhs(){
//     lobhs.forEach(function(data,index){
//         var coords = data.latlng;
//         var marker = new kakao.maps.Marker({
//             map : map,
//             position : coords,
//             image : lobhsmarkerImage
//         });
//         marker.setMap(map);

//         var customOverlay = new kakao.maps.InfoWindow({
//             content : '<span class="info-title">'+lobhs[index].title+'<span>'
//         }); 
//         customOverlay.setMap(map);
//         var infoTitle = document.querySelectorAll('.info-title');
//         infoTitle.forEach(function(e) {
//             var w = e.offsetWidth+5;
//             var ml = w/2;
//             e.parentElement.style.top = "20px";
//             e.parentElement.style.left = "50%";
//             e.parentElement.style.marginLeft = -ml+"px";
//             e.parentElement.style.width = w+"px";
//             e.parentElement.previousSibling.style.display = "none";
//             e.parentElement.parentElement.style.border = "0px";
//             e.parentElement.parentElement.style.background = "unset";
//         });

//         map.setCenter(new kakao.maps.LatLng(37.51112, 127.095973));

//         kakao.maps.event.addListener(marker, 'mouseover', function(){
//             customOverlay.open(map,marker);
//         })
//         kakao.maps.event.addListener(marker, 'mouseout', function(){
//             customOverlay.close();
//         })
//     });
// }


//메뉴에 있는 Marker를 선택하는 경우
function changeMarker(type) {
    var lobhs = document.getElementById('lobhs');
    var department = document.getElementById('department');
    var mart = document.getElementById('mart');
    var seven = document.getElementById('seven');
    var ria = document.getElementById('ria');
    var hotel = document.getElementById('hotel');
    var all = document.getElementById('all');

    if (type == 'lobhs') {
        lobhs.className = "menu_selected";
        department.className = "";
        mart.className = "";
        seven.className = "";
        ria.className = "";
        hotel.className = "";
        all.className = "";

        setLobhsMarker(map);
        setDepartmentMarker(null);
        setMarttMarker(null);
        setRiatMarker(null);
        setSeventMarker(null);
        setRiatMarker(null);
        setHotelMarker(null);
    }
    else if (type == 'department') {
        lobhs.className = "";
        department.className = "menu_selected";
        mart.className = "";
        seven.className = "";
        ria.className = "";
        hotel.className = "";
        all.className = "";

        setLobhsMarker(null);
        setDepartmentMarker(map);
        setMarttMarker(null);
        setSeventMarker(null);
        setRiatMarker(null);
        setHotelMarker(null);
    }
    else if (type == 'mart') {
        lobhs.className = "";
        department.className = "";
        mart.className = "menu_selected";
        seven.className = "";
        ria.className = "";
        hotel.className = "";
        all.className = "";

        setLobhsMarker(null);
        setDepartmentMarker(null);
        setMarttMarker(map);
        setSeventMarker(null);
        setRiatMarker(null);
        setHotelMarker(null);
    }
    else if (type == 'seven') {
        lobhs.className = "";
        department.className = "";
        mart.className = "";
        seven.className = "menu_selected";
        ria.className = "";
        hotel.className = "";
        all.className = "";

        setLobhsMarker(null);
        setDepartmentMarker(null);
        setMarttMarker(null);
        setSeventMarker(map);
        setRiatMarker(null);
        setHotelMarker(null);
    }
    else if (type == 'ria') {
        lobhs.className = "";
        department.className = "";
        mart.className = "";
        seven.className = "";
        ria.className = "menu_selected";
        hotel.className = "";
        all.className = "";

        setLobhsMarker(null);
        setDepartmentMarker(null);
        setMarttMarker(null);
        setSeventMarker(null);
        setRiatMarker(map);
        setHotelMarker(null);
    }
    else if (type == 'hotel') {
        lobhs.className = "";
        department.className = "";
        mart.className = "";
        seven.className = "";
        ria.className = "";
        hotel.className = "menu_selected";
        all.className = "";

        setLobhsMarker(null);
        setDepartmentMarker(null);
        setMarttMarker(null);
        setSeventMarker(null);
        setRiatMarker(null);
        setHotelMarker(map);
    }
    else if (type == 'all') {
        lobhs.className = "";
        department.className = "";
        mart.className = "";
        seven.className = "";
        ria.className = "";
        hotel.className = "";
        all.className = "menu_selected";

        setLobhsMarker(map);
        setDepartmentMarker(map);
        setMarttMarker(map);
        setSeventMarker(map);
        setRiatMarker(map);
        setHotelMarker(map);
    }
}