import Head from 'next/head'

import Menu from '../components/Menu';

export default function Layout(props) {
    return (
        <div>
            <Head>
                <title> {props.title} </title>
            </Head>

            <Header isHome={props.isHome} />

            <Menu />

            <main>
                {props.children}
            </main>


        </div>
    )
}

function Header(props) {
    if (props.isHome) {
        return (
            <HomeHeader />
        );
    } else {
        return (
            <JustHeader />
        );
    }
}

function HomeHeader(props) {
    return (
        <div>
            <header className="text-center bg-fixed bg-center h-screen items-center">
                <div className="flex justify-center pt-8 pb-8">
                    <img src="/images/kreimben_memoji.jpeg" className="rounded-full flex justify-center w-40 h-40 shadow-2xl"></img>
                </div>
                <p className="text-2xl font-light font-mono bg-white bg-opacity-50 rounded-lg px-3 py-2 inline-block">Kreimben.com, Indie developer's website</p>
            </header>
            <style jsx>
                {`
                
                header {
                    background-image: url('/images/backgroundImage.jpg');
                }
                
                `}
            </style>
        </div>
    );
}

function JustHeader(props) {
    return (
        <div>
            <header className="text-center bg-cover bg-center h-auto items-center">
                <div className="flex justify-center py-8">
                    <img src="/images/kreimben_memoji.jpeg" className="rounded-full flex justify-center w-40 h-40 shadow-2xl"></img>
                </div>
                <p className="text-2xl font-light font-mono bg-white bg-opacity-50 rounded-lg px-3 py-2 mb-8 inline-block">Kreimben.com, Indie developer's website</p>
            </header>
            <style jsx>
                {`
                
                header {
                    background-image: url('/images/backgroundImage.jpg');
                }
                
                `}
            </style>
        </div>
    );
}