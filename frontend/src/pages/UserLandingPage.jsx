import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import {Link, useNavigate} from 'react-router-dom';
import { toast } from 'react-toastify';
import Loader from '../components/Loader/Loader';
import axios from '../helper/axios-helper.js';
import useLoading from '../hook/customHook';
import './SingleProduct.css';
import {backendURL} from "../helper/utils";
const UserLandingPage = () => {
    const isLoading = useLoading();
    const navigate = useNavigate();
    const storeData = useSelector(state => state.auth);
    const [loading, setLoading] = useState(false);
    const [shop, setShop] = useState([]);

    const [filter, setFilter] = useState('All');
    const [searchTerm, setSearchTerm] = useState('');
    const [currentPage, setCurrentPage] = useState(1);

    useEffect(() => {
        setLoading(true);

        let apiUrl = '/shops/';  // Updated to fetch from the new endpoint

        apiUrl += `?page=${currentPage}`;

        if (searchTerm) {
            apiUrl += `&search=${searchTerm}`;
        }

        axios.get(apiUrl)
            .then(response => {
                console.log(response.data)
                setShop(response.data.results);  // Update to use the paginated response
            })
            .catch(error => {
                console.error('Error fetching shops:', error);
            });

        setLoading(false);

    }, [searchTerm, currentPage]);


    const handleSearchChange = (event) => {
        setSearchTerm(event.target.value);
        setCurrentPage(1);
    };
    const handlePageChange = (pageNumber) => {
        setCurrentPage(pageNumber);
    };
    function renderStars(rating) {
        const stars = [];
        const roundedRating = Math.round(rating * 2) / 2; // Round to nearest 0.5

        for (let i = 1; i <= 5; i++) {
            if (i <= roundedRating) {
                // Full star
                stars.push(<span key={i} className="fas fa-star checked"></span>);
            } else if (i - 0.5 === roundedRating) {
                // Half star
                stars.push(<span key={i} className="fas fa-star-half-alt checked"></span>);
            } else {
                // No rating star
                stars.push(<span key={i} className="fa-regular fa-star checked"></span>);
            }
        }

        return stars;
    }
    const renderPagination = () => {
        const totalPages = Math.ceil(shop?.count / 6);
        if (totalPages <= 1) {
            return null;
        }

        const pageNumbers = [];
        for (let i = 1; i <= totalPages; i++) {
            pageNumbers.push(
                <li key={i} >
                    <span className={currentPage === i ? 'pagination-btn active' : 'pagination-btn'} onClick={() => handlePageChange(i)}>{i}</span>
                </li>
            );
        }

        return (
            <div className="pagination-wrap">
                <ul>
                    <li>
                        <button disabled={currentPage === 1} onClick={() => handlePageChange(currentPage - 1)} className={currentPage === 1 ? 'pagination-btn disabled' : 'pagination-btn '}>
                            Prev
                        </button>
                    </li>
                    {pageNumbers}
                    <li>
                        <button disabled={currentPage === totalPages} onClick={() => handlePageChange(currentPage + 1)} className={currentPage === totalPages ? 'pagination-btn disabled' : 'pagination-btn '}>
                            Next
                        </button>
                    </li>
                </ul>
            </div>
        );
    };
    const exploreShop = (id,name) => {
        navigate('/shop/'+ id +'?name='+name);
    }
    return (
        <>
            {(isLoading) && <Loader />}

            <div class="breadcrumb-section breadcrumb-bg">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-8 offset-lg-2 text-center">
                            <div class="breadcrumb-text">
                                <p>Fresh and Organic</p>
                                <h1>Shop</h1>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="product-section mt-100 mb-150">
                <div class="container">

                    <div class="row">

                        <div class="col-lg-8 offset-lg-2 text-center" style={{ marginTop: '50px' }}>
                            <div class="section-title">
                                <h3><span class="orange-text">Our</span> Shop</h3>
                            </div>
                        </div>
                        <div class="col-md-12 mb-20">
                            <div class="product-filters">
                                <ul>
                                    <li>
                                        <i className="fas fa-search" style={{ marginRight: '10px' }}></i>
                                        <input
                                            type="text"
                                            placeholder="Search Shop"
                                            value={searchTerm}
                                            onChange={handleSearchChange}
                                            style={{ border: 'none', outline: 'none' }}
                                        />
                                    </li>
                                </ul>
                            </div>
                        </div>

                        <div class="col-lg-12 col-md-12 product-lists">
                            {loading ? <p>Loading</p> :
                                shop?.map(sp => (
                                    <div key={sp.id} className="col-lg-4 col-md-6 text-center">
                                        <div className="single-product-item">
                                            <div className="product-image">
                                                <Link to={'/shop/'+ sp.id +'?name='+ sp.name}><img src={`${backendURL}`+`${sp.profile_pic}`} alt={sp.name} /> </Link>
                                            </div>

                                            <h3>{sp.name}</h3>
                                            <div className="rating">
                                                {/* Render the star icons based on the rating */}
                                                {renderStars(sp.average_rating)}
                                            </div>
                                            <br />
                                            <span class="cart-btn" onClick={() => exploreShop(sp.id,sp.name)}><i class="fas fa-shopping-cart"></i> Explore Shop</span>
                                        </div>
                                    </div>
                                ))}
                        </div>

                        <div class="row w-100">
                            <div class="col-lg-12 text-center">
                                {renderPagination()}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>

    );
};

export default UserLandingPage;