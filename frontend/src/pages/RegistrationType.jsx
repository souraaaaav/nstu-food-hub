import React from 'react';
import { useNavigate } from 'react-router-dom'; // Import useHistory hook from react-router-dom

const RegistrationType = () => {
    const navigate = useNavigate();
    return (
        <>
            <div class="breadcrumb-section breadcrumb-bg">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-8 offset-lg-2 text-center">
                            <div class="breadcrumb-text">
                                <p>Join With us </p>
                                <h1>Crreate Account</h1>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="checkout-section mt-100 mb-150">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-9 mx-auto text-center">
                            <div class="checkout-accordion-wrap">
                                <div className="accordion" id="accordionExample">

                                    <div className="card single-accordion">
                                        <div className="card-header" id="headingOne">

                                            <h5 onClick={() => {
                                                navigate('/registration-restaurant');
                                            }} className='create-post-submit-btn'>
                                                <span>
                                                    Registration for Restaurant
                                                </span>
                                            </h5>
                                        </div>
                                    </div>

                                    <div className="card single-accordion">
                                        <div className="card-header" id="headingOne">

                                            <h5 onClick={() => {
                                                navigate('/registration');
                                            }} className='create-post-submit-btn'>
                                                <span>
                                                    Registration as Customer
                                                </span>
                                            </h5>
                                        </div>
                                    </div>
                                    <div className="card single-accordion">
                                        <div className="card-header" id="headingOne">

                                            <h5 className='create-post-submit-btn' onClick={() => {
                                                navigate('/registration-delivery-man');
                                            }}>
                                                <span>
                                                    Registration as Delivery man
                                                </span>
                                            </h5>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
};

export default RegistrationType;