import Nav from '@app/components/nav';

const RootLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <main className="bg-gray-900 text-white">
      <Nav></Nav>
      {children}
    </main>
  );
};

export default RootLayout;
