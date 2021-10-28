/*!
* Start Bootstrap - Shop Homepage v5.0.4 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

$(function () {

    if (localStorage.getItem('count')==null){
            localStorage.setItem('count','0')
        console.log(localStorage)
        }

    $('.badge').append(localStorage.getItem('count'))

    $.get(`https://reqres.in/api/users`, function (data, status) {
        $.each(data.data, function (index, value) {
            let card = `<div class="col mb-5">
                <div class="card h-100">
                    <img class="card-img-top" src=${value.avatar} alt="..."/>
                  
                    <div class="card-body p-4">
                        <div class="text-center">
                           
                            <h5 class="fw-bolder">${value.first_name + " " + value.last_name}</h5>
                     
                            ${value.email}
                        </div>
                    </div>
                    <!-- Product actions-->
                    <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                        <div class="text-center"><button type="button" class="btn btn-outline-dark mt-auto mx-2 basket" product_id=${value.id}>add to basket</button>
                        <button type="button" class="btn btn-outline-info open"  data-toggle="modal" data-target="#editmodal" product_id=${value.id} >
                              Detail
                        </button>                       
                        
                        
                        </div>
                    </div>
                </div>
            </div>`
            // console.log(index)
            $('#show-cards').append(card)
        })
        $('.open').click(function () {
            $.get(`https://reqres.in/api/users/${$(this).attr('product_id')}`, function (data, status) {
                user_email=data.data.email
                previous_text=$('.modal-body').text()
                console.log(previous_text)
                $('.modal-body').text(function () {
                    return $(this).text().replace(previous_text,user_email)
                })
            })
            $('#editmodal').modal('show')
        })



        $('.basket').click( function () {
            let user_id = $(this).attr('product_id')
            console.log(localStorage)
               let  amount=localStorage.getItem('count');
               let new_amount=parseInt(amount)+1
                 localStorage.setItem( 'count', new_amount);
               $('.badge').text(function (){
                return  $(this).text().replace(amount, new_amount)
            })
        })
    })


})