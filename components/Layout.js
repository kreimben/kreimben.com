import Head from 'next/head'

import Menu from '../components/Menu';

export default function Layout(props) {
    return (
        <div>
            <Head>
                <title> {props.title} </title>
            </Head>

            <header className="text-center bg-fixed bg-center h-screen items-center">
                    <div className="w-full flex justify-center py-16">
                        <img src="/images/kreimben_memoji.jpeg" className="rounded-full flex justify-center w-40 h-40 shadow-2xl"></img>
                    </div>
                    <p className="text-2xl font-light font-mono bg-white bg-opacity-50 rounded-lg px-3 py-2 inline-block">Kreimben.com, Indie developer's website</p>
            </header>

            <Menu />

            <main>
                {props.children}
            </main>

            <style jsx>
                {`
                
                header {
                    background-image: url('/images/backgroundImage.jpg');
                }
                
                `}
            </style>

        </div>
    )
}