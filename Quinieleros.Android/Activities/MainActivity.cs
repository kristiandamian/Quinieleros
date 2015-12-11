using System;

using Android.App;
using Android.Content;
using Android.Runtime;
using Android.Views;
using Android.Widget;
using Android.OS;
using Android.Support.V7.App;
using Android.Support.V7.AppCompat;
using Android.Support.V7.Widget;
using Android.Support.V4.App;
using Android.Support.V4.Widget;
using Android.Support.Design.Widget;

namespace Quinieleros
{
	[Activity (Label = "Quinieleros", MainLauncher = true, Icon = "@drawable/icon", Theme = "@style/MyTheme")]
	public class MainActivity : BaseActivity
    {
        DrawerLayout drawerLayout;
        NavigationView navigationView;

        protected override int LayoutResource {
			get {
				return Resource.Layout.MenuSlide;
			}
		}

		protected override void OnCreate (Bundle savedInstanceState)
		{
			Xamarin.Insights.Initialize (BO.Insights.ApiKey, this);
			base.OnCreate (savedInstanceState);


            drawerLayout = FindViewById<DrawerLayout>(Resource.Id.drawer_layout);

            SupportActionBar.SetHomeAsUpIndicator(Resource.Drawable.ic_menu);
            navigationView = FindViewById<NavigationView>(Resource.Id.nav_view);

            navigationView.NavigationItemSelected += (sender, e) => {
                e.MenuItem.SetChecked(true);

                switch (e.MenuItem.ItemId)
                {
                    case Resource.Id.nav_Resultados:
                        ListItemClicked(0);
                        break;
                    case Resource.Id.nav_CrearGrupo:
                        ListItemClicked(1);
                        break;
                    case Resource.Id.nav_MisGrupos:
                        ListItemClicked(2);
                        break;
                    case Resource.Id.nav_estadisticas:
                        ListItemClicked(3);
                        break;
                }
                drawerLayout.CloseDrawers();
            };


            // Set our view from the "main" layout resource
            SetContentView(Resource.Layout.Main);
			// Get our button from the layout resource,
			// and attach an event to it
			Button button = FindViewById<Button> (Resource.Id.myButton);
		}
        private void ListItemClicked(int position)
        {
            Android.Support.V4.App.Fragment fragment = null;
            switch (position)
            {
                case 0:
                    //fragment = new Facturar();
                    break;
                case 1:
                    //fragment = new VerFacturas();
                    break;
                case 2:
                    //fragment = new Configuracion();
                    break;
                case 3:
                    //fragment = new ComprarFacturas();
                    break;
            }
            SupportFragmentManager.BeginTransaction()
                .Replace(Resource.Id.content_frame, fragment)
                .SetTransition(Android.Support.V4.App.FragmentTransaction.TransitFragmentFade)
                .Commit();
        }



        public override bool OnOptionsItemSelected(IMenuItem item)
        {
            switch (item.ItemId)
            {
                case Android.Resource.Id.Home:
                    drawerLayout.OpenDrawer(Android.Support.V4.View.GravityCompat.Start);
                    return true;
            }
            return base.OnOptionsItemSelected(item);
        }

    }
}
