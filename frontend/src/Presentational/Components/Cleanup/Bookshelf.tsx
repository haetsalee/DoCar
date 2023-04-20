import React, { useState, useEffect } from 'react';
import axios from 'axios';
import BookItem from './BookItem';
import * as BookStyle from './BookList_Style';
import Btn from './../../Common/Btn';
import { useParams, useNavigate, Link } from 'react-router-dom';
import Swal from 'sweetalert2';
import withReactContent from 'sweetalert2-react-content';
import BookTable from './../BookTable';
import BookTableBack from './../BookTableBack';

type recipeParams = {
  params: string;
};

function Bookshelf() {
  const [books, setBooks] = useState<[]>([]);
  const { id } = useParams() as { id: string };

  const navigate = useNavigate();

  const GetBooks = () => {
    axios.get('https://jsonplaceholder.typicode.com/todos').then((res) => {
      setBooks(res.data);
      console.log(res.data);
    });
  };

  const MySwal = withReactContent(Swal);

  // 다음 책장으로 가는 모달
  const setModal = () => {
    MySwal.fire({
      title: '모든 책을 정리하셨습니까?',
      // timer: 1500,
      timerProgressBar: true,
      // showConfirmButton: false,
      showCancelButton: true,
      showConfirmButton: true,
      cancelButtonText: '아니오',
      confirmButtonText: '네',
      allowOutsideClick: false,
      html: <div></div>,
    }).then((result) => {
      if (result.isConfirmed) {
        // 확인 버튼을 눌렀을 때,
        MySwal.fire({
          icon: 'success',
          title: '책장 정리 완료!',
          // timer: 1500,
          timerProgressBar: true,
          // showConfirmButton: false,
          showCancelButton: true,
          showConfirmButton: true,
          cancelButtonText: '정리 종료',
          confirmButtonText: '다음 책장으로 이동',
          allowOutsideClick: false,
          html: <div></div>,
        }).then((result) => {
          if (result.isConfirmed) {
            // 확인 버튼을 눌렀을 때,
            // 확인 버튼을 누르면 axios로 다음 책장을 받는다.
            console.log(result); // 다음 책장이 있으면 다음 페이지로 넘어가고, 없으면 마무리 페이지로 간다.
            axios
              .get('https://jsonplaceholder.typicode.com/todos')
              .then((res) => {
                // setBooks(res.data);
                console.log('도서 정리 완료 요청 성공');
                navigate(`/cleanup/2`);
              });
          } else {
            navigate(`/cleanup/end`);
          }
        });
      } else {
      }
    });
  };

  // 중간에 탈주하는 모달
  const setCheckModal = () => {
    MySwal.fire({
      title: '현재 정리된 책을 체크해주세요',
      timerProgressBar: true,
      showCancelButton: true,
      showConfirmButton: true,
      cancelButtonText: '취소',
      confirmButtonText: '반납하기',
      allowOutsideClick: false,
      html: (
        <>
          <BookTableBack />
        </>
      ),
    }).then((result) => {
      if (result.isConfirmed) {
        // 확인 버튼을 눌렀을 때,
        // 확인 버튼을 누르면 axios로 다음 책장을 받는다.
        MySwal.fire({
          title: '반납된 책이 맞습니까?',
          timerProgressBar: true,
          showCancelButton: true,
          showConfirmButton: true,
          cancelButtonText: '아니오',
          confirmButtonText: '네',
          allowOutsideClick: false,
          html: (
            <>
              <BookTableBack />
            </>
          ),
        }).then((result) => {
          if (result.isConfirmed) {
            // 확인 버튼을 눌렀을 때,
            // 확인 버튼을 누르면 axios로 다음 책장을 받는다.
            console.log(result); // 다음 책장이 있으면 다음 페이지로 넘어가고, 없으면 마무리 페이지로 간다.
            axios
              .get('https://jsonplaceholder.typicode.com/todos')
              .then((res) => {
                // setBooks(res.data);
                console.log('도서 정리 완료 요청 성공');
                navigate(`/cleanup/end`);
              });
          } else {
            setCheckModal();
          }
        });
      } else {
        MySwal.fire({
          title: '실팽',
        });
      }
    });
  };

  useEffect(() => {
    GetBooks();
  }, []);

  return (
    <BookStyle.WrapClean>
      <Btn
        message="원위치로"
        go={() => {
          setCheckModal();
        }}
        position="absolute"
        top="-20px"
        right="18px"
      />
      <BookStyle.Title>{id}번 책장 반납도서</BookStyle.Title>
      {/* {books && (
        <BookStyle.WrapBooks>
          {books.map((book) => (
            <BookItem book={book} />
          ))}
        </BookStyle.WrapBooks>
      )} */}
      <BookTable />

      {/* 여기서 이동할 때 이동해야할 책장 경로 */}
      <Btn
        message={`정리완료`}
        go={() => {
          setModal();
        }}
        position="absolute"
        bottom="20px"
      />
      {/* 모달 띄어서 다음 책장으로 이동시키기 */}
    </BookStyle.WrapClean>
  );
}

export default Bookshelf;
