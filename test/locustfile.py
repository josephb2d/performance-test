from locust import HttpUser, TaskSet, task, between
import json


class Purchase(TaskSet):

	def on_start(self):
		self.client.post('/api/login', {
			'remember': True,
			'type': 'email',
			'username': '<Username>',
			'password': '<Password>'
		})

	@task
	def swaggerDocs(self):
		# user should be logged in here (unless the USER_CREDENTIALS ran out)
		self.client.get('/api-docs')

	@task
	def reporting(self):
		self.client.get('/reporting')

	@task
	class Purchase(TaskSet):
		@task
		def purchaseItem(self):
			basketItem = json.dumps({'offerId': 4822,'quantity': 1,'basketId': 2576,'fulfillmentInfo': {'isShipping': True,'shippingSettingId': 320,'isRecurringSubscription': False,'isUpfrontSubscription':False},'fulfillmentDate': None,'mobileLogin': True,'snapshot': {'title': 'Chicken breast','size': '1','minPrice': '0.00','maxPrice': '0.00','isWeightedItem': False,'minWeight': '1.00','maxWeight': '0.00','pricePerLb': '8.00','buyerTypeId': 1,'pickupLocationStreetAddress1': None,'pickupLocationCity': None,'pickupLocationState': None,'pickupLocationPostalCode': None,'deliveryCharge': None,'freeDeliveryOrderMinimum': None,'largeImgId': 6801,'description': '%3Cp%3EChicken%20Breast%3C%2Fp%3E%0A','barn2DoorPrice': '8','useIntegratedDeliveryCharges': True,'useIntegratedTaxes': True},'sellerId': 870,'useAsDefault': False,'needsRedirect': False,'viewType': 'all','sellerSubCategoryId': 744})
			# Add item to purchase
			self.client.post('/basket/item', json.dumps({'offerId': 4822,'quantity': 1,'basketId': 2576,'fulfillmentInfo': {'isShipping': True,'shippingSettingId': 320,'isRecurringSubscription': False,'isUpfrontSubscription':False},'fulfillmentDate': None,'mobileLogin': True,'snapshot': {'title': 'Chicken breast','size': '1','minPrice': '0.00','maxPrice': '0.00','isWeightedItem': False,'minWeight': '1.00','maxWeight': '0.00','pricePerLb': '8.00','buyerTypeId': 1,'pickupLocationStreetAddress1': None,'pickupLocationCity': None,'pickupLocationState': None,'pickupLocationPostalCode': None,'deliveryCharge': None,'freeDeliveryOrderMinimum': None,'largeImgId': 6801,'description': '%3Cp%3EChicken%20Breast%3C%2Fp%3E%0A','barn2DoorPrice': '8','useIntegratedDeliveryCharges': True,'useIntegratedTaxes': True},'sellerId': 870,'useAsDefault': False,'needsRedirect': False,'viewType': 'all','sellerSubCategoryId': 744}))
			# Initialize basket items for purchase.
			self.client.get('/purchase/init?basketId=2576&sellerId=870&userId=1756')
			# Purchase Items
			self.client.post('/purchase', {
				'mobileLogin': True,
				'useCredits': False,
				'basketId': 2576,
				'userId': 1756,
				'addressId': 6003,
				'buyerPayFee': False,
				'stripeIdempotencyKey': '7c796170-16c5-4ab7-9c65-b271ce594733',
				'cardId': 'card_1HjWhkHLtEMFPoSaAYYTfZgc',
				'paymentOption': 'creditCard',
				'address': {
					'firstName': 'Joseph',
					'lastName': 'Hoang',
					'streetAddress1': '520 pike st',
					'city': 'seattle',
					'state': 'WA',
					'postalCode': '98104',
					'phone': '(555) 555-5555'
				}
			})

class User(HttpUser):
	tasks = [Purchase]
	wait_time = between(5, 60)
