


$("#search").click(function()
    {

$.ajax({ 
           

            type:"post",
            dataType:"json",
            url: url_now,
            data: "state=zippedfile&folderName="+folderName,
            success: function(data){
                window.location.href = data.result; 
        }

                    
            

           });


});







var districts =['Taplejung','Panchthar','Ilam','Jhapa','Morang','Sunsari','Dhankuta','Terhathum','Sankhuwasabha','Bhojpur','Solukhumbu','Okhaldhunga','Khotang','Udayapur','Saptari','Siraha','Dhanusha','Mahottari','Sarlahi','Sindhuli','Ramechhap','Dolakha','Sindhupalchok','Kavrepalanchok','Lalitpur','Bhaktapur','Kathmandu','Nuwakot','Rasuwa','Dhading','Makwanpur','Rautahat','Bara','Parsa','Chitwan','Gorkha','Lamjung','Tanahu','Syangja','Kaski','Manang','Mustang','Myagdi','Parbat','Baglung','Gulmi','Palpa','Nawalparasi','Rupandehi','Kapilbastu','Arghakhanchi','Pyuthan','Rolpa','Rukum','Salyan','Dang','Banke','Bardiya','Surkhet','Dailekh','Jajarkot','Dolpa','Jumla','Kalikot','Mugu','Humla','Bajura','Bajhang','Achham','Doti','Kailali','Kanchanpur','Dadeldhura','Baitadi','Darchula'];

