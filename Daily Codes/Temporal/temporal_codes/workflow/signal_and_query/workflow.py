import asyncio
from temporalio import workflow

@workflow.defn
class ProductsLeft:
    def __init__(self):
        self.products = 0

    @workflow.run
    async def run(self, products: int) -> int:
        self.products = products
        while self.products > 0:
            await asyncio.sleep(1)
            print(self.products)
        return self.products

    @workflow.signal
    async def update_products(self, new_products: int):
        print(f"Received a signal to update the products to {new_products}")
        self.products = new_products
    
    @workflow.query
    async def get_product_count(self) -> int:
        print(f"Received a query to get the products left")
        return self.products

