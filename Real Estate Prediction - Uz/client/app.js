function getLevelValue() {
    var uiLevel = document.getElementsByName("uiLevel");
    for(var i in uiLevel) {
      if(uiLevel[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }

function getRoomValue() {
    var uiRooms = document.getElementsByName("uiRooms");
    for(var i in uiRooms) {
        if(uiRooms[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1; // Invalid Value
}


function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var size = document.getElementById("uiSize").value;
    var rooms = getRoomValue();
    var level = getLevelValue();
    var district = document.getElementById("uiDistrict").value;
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_home_price";

    $.ajax({
        url: url,
        type: "POST",
        contentType: 'application/json',
        data: JSON.stringify({
            rooms: rooms,
            size: size,
            level: level,
            district: district.value
        }),
        success: function(data, status) {
            console.log(data.estimated_price);
            $("#estPrice").html("<h2>" + data.estimated_price.toString() + " USD </h2>");
            console.log(status);
        },
        error: function(xhr, status, error) {
            console.log(error);
        }
    });
function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var district = data.district;
            var uiDistrict = document.getElementById("uiDistrict");
            $('#uiDistrict').empty();
            for(var i in district) {
                var opt = new Option(district[i]);
                $('#uiDistrict').append(opt);
            }
        }
    });
  }

  window.onload = onPageLoad;
}