createLobhsMarker();
createDeparmentMarker();
createMartMarker();
createSevenMarker();
createRiaMarker();
createHotelMarker();

initMarker(request_company);
// if(request_company.length == 1) {
//     console.log(request_company[0]);
//     initMarker(request_company[0]);
// }
// else {
//     initMarker('all');
// }


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
        kakao.maps.event.addListener(marker, 'click', clickListener(marker, lobhs[i].title, lobhs[i].company));
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
        kakao.maps.event.addListener(marker, 'click', clickListener(marker, department[i].title, department[i].company));
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
        iwContent = '<div class="info-title" style="padding:1px;text-align:center;width:180px">' + mart[i].title + '</div>'
        var infowindow = new kakao.maps.InfoWindow({
            position: mart[i].latlng,
            content: iwContent,
        });
        martInfowindow.push(infowindow);
        kakao.maps.event.addListener(marker, 'mouseover', makeOverListner(map, marker, infowindow));
        kakao.maps.event.addListener(marker, 'mouseout', makeOutListener(infowindow));
        kakao.maps.event.addListener(marker, 'click', clickListener(marker, mart[i].title, mart[i].company));
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
        kakao.maps.event.addListener(marker, 'click', clickListener(marker, seven[i].title, seven[i].company));
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
        kakao.maps.event.addListener(marker, 'click', clickListener(marker, ria[i].title, ria[i].company));
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
        kakao.maps.event.addListener(marker, 'click', clickListener(marker, hotel[i].title, hotel[i].company));
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
function clickListener(marker, shop, comapny) {
    return function () {
        map.setCenter(marker.getPosition()) //해당 지점을 기준으로 지도 중심 이동
        alert(shop + " " + comapny+ "을 선택하셨습니다.");
    }
}

//메뉴에 있는 Marker를 선택하는 경우
function initMarker(types) {
    var lobhs = document.getElementById('lobhs');
    var department = document.getElementById('department');
    var mart = document.getElementById('mart');
    var seven = document.getElementById('seven');
    var ria = document.getElementById('ria');
    var hotel = document.getElementById('hotel');
    var all = document.getElementById('all');
    lobhs.className = "";
    department.className = "";
    mart.className = "";
    seven.className = "";
    ria.className = "";
    hotel.className = "";
    all.className = "";

    setLobhsMarker(null);
    setDepartmentMarker(null);
    setMarttMarker(null);
    setRiatMarker(null);
    setSeventMarker(null);
    setRiatMarker(null);
    query_company_list = types;

    if(types.length == COMPANY_CNT || types.length == 0) {
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
        setRiatMarker(map);
        setSeventMarker(map);
        setRiatMarker(map);
        return;
    }

    types.forEach(type => {
        console.log(type);
        if (type == '롭스') {
            lobhs.className = "menu_selected";
            setLobhsMarker(map);
        }
        else if (type == '롯데백화점') {
            department.className = "menu_selected";
            setDepartmentMarker(map);
        }
        else if (type == '롯데마트') {
            mart.className = "menu_selected";
            setMarttMarker(map);
        }
        else if (type == '세븐일레븐') {
            seven.className = "menu_selected";
            setSeventMarker(map);
        }
        else if (type == '롯데리아') {
            ria.className = "menu_selected";
            setRiatMarker(map);
        }
        else if (type == '롯데호텔') {
            hotel.className = "menu_selected";
            setHotelMarker(map);
        }
    });
}


function filterOnClick(type) {
    
    let idx = query_company_list.indexOf(type);
    if (type == 'all') {
        query_company_list = ["롭스", "롯데백화점", "롯데마트", "세븐일레븐", "롯데리아", "롯데호텔"]
    } 
    else if(idx > -1) {
        if(query_company_list.length == COMPANY_CNT) {
            query_company_list = [type];
        }
        else {
            query_company_list.splice(idx, 1);
            if(query_company_list.length == 0) {
                query_company_list.push(type);
            }
        }
    }
    else {
        query_company_list.push(type);
    }

    query_company_str = ""
    for(var i = 0; i < query_company_list.length; i++) {
        query_company_str += "company="+query_company_list[i]+"&";
    }
    query_str = "/?page="+page+"&page_cnt="+page_cnt+"&"+query_company_str;

    if(sort && sort!= "undefined") {
        query_str += "sort=" + sort + "&";
    }
    else {
        query_str += "sort=추천순&"
    }
    if(lat && lat!="undefined") {
        query_str += "lat=" + lat + "&";
    }
    else {
        lat = cur_lat;
        query_str += "lat=" + lat + "&";
    }
    if(lng && lng!="undefined") {
        query_str += "lng=" + lng + "&";
    }
    else {
        lng = cur_lng;
        query_str += "lng=" + lng + "&";
    }
    window.location = query_str;
}

function sortFilterOnClick(type) {
    sort = type;

    query_company_str = ""
    for(var i = 0; i < query_company_list.length; i++) {
        query_company_str += "company="+query_company_list[i]+"&";
    }
    query_str = "/?page="+page+"&page_cnt="+page_cnt+"&"+query_company_str;

    if(sort && sort!= "undefined") {
        query_str += "sort=" + sort + "&";
    }
    else {
        query_str += "sort=추천순&"
    }
    if(lat && lat!="undefined") {
        query_str += "lat=" + lat + "&";
    }
    else {
        lat = cur_lat;
        query_str += "lat=" + lat + "&";
    }
    if(lng && lng!="undefined") {
        query_str += "lng=" + lng + "&";
    }
    else {
        lng = cur_lng;
        query_str += "lng=" + lng + "&";
    }
    window.location = query_str;
}

function pagination(p) {
    page = p;
    query_company_str = ""
    for(var i = 0; i < query_company_list.length; i++) {
        query_company_str += "company="+query_company_list[i]+"&";
    }
    query_str = "/?page="+page+"&page_cnt="+page_cnt+"&"+query_company_str;

    if(sort && sort!= "undefined") {
        query_str += "sort=" + sort + "&";
    }
    else {
        query_str += "sort=추천순&"
    }
    if(lat && lat!="undefined") {
        query_str += "lat=" + lat + "&";
    }
    else {
        lat = cur_lat;
        query_str += "lat=" + lat + "&";
    }
    if(lng && lng!="undefined") {
        query_str += "lng=" + lng + "&";
    }
    else {
        lng = cur_lng;
        query_str += "lng=" + lng + "&";
    }
    window.location = query_str;

}