import Logo from '../assets/Icons/Logo.svg'
// import Manrope from '../assets/Fonts/Manrope.ttf'

const Home = () => {

  return (
    <div className=''>
    <header className=' w-full bg-white flex flex-col justify-center items-center'>
      <nav className='w-5/6 h-[15vh] flex justify-between space-x-4 border-b-2 border-blue-500 '>
        <img className=' size-20' src={Logo} alt="logo img" />
        {/* nav link */}
        <ul className='w-full flex justify-evenly  items-center ml-20  '>
          <li><a href="#">Location</a></li>
          <li><a href="#">Blogs</a></li>
          <li><a href="#">Testimonial</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>

      <div>
        <h1>Home That Makes <br /> You Living Life!</h1>
        <p>
          Are you looking for amazing Real estate? Don't worry we got it for you
        </p>
        <button>Learn More</button>
      </div>
    </header>
    </div>
  )
}

export default Home