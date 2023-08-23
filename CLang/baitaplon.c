#include <stdio.h>
#include <string.h>
#define pi 3.1415926535

int socapban(int n, int ld);
void wind(int n, int dc, int dg, int ld, FILE *fo);
void rain(int n, int dc, int dg, int ld, FILE *fo);
void sun(int n, int dc, int dg, int ld, FILE *fo);
void fog(int n, int dc, int dg, FILE *fo);
void cloud(int n, int dc, int dg, int ld, FILE *fo);

int main()
{	
	FILE *fi, *fo;
	
	fi = fopen("input.inp", "r");
	fo = fopen("output.out", "w");
	
	//Doc du lieu
	int n, dc, dg, ld;
	char w[10];
	
	fscanf(fi, "%d", &n);
	fscanf(fi, "%d", &dc);
	fscanf(fi, "%d", &dg);
	fscanf(fi, "%d", &ld);
	fscanf(fi, "%s", &w);
			
	//Kiem tra
	if((n < 0 || n > 1000) || (ld < 1 || ld > 300))
	{
		fprintf(fo, "-1 -1 %d", n);
	}

	//In ket qua neu input dung
	if((n >= 0 && n <= 1000) && (ld >= 1 && ld <= 300))
	{
		if(strcmp(w, "Wind") == 0)
		{
			wind(n, dc, dg, ld, fo);
		}
		else if(strcmp(w, "Rain") == 0)
		{
			rain(n, dc, dg, ld, fo);
		}
		else if(strcmp(w, "Sun") == 0)
		{
			sun(n, dc, dg, ld, fo);
		}
		else if(strcmp(w, "Fog") == 0)
		{
			fog(n, dc, dg, fo);
		}
		else
		{
			cloud(n, dc, dg, ld, fo);
		}
	}
		
	fclose(fi);
	fclose(fo);
	
	return 0;
}

//Wind----------------------------------------------
void wind(int n, int dc, int dg, int ld, FILE *fo)
{
	int bc, bg, i, bc_m, bg_m, ld_d;
	float nc_c, nc_g, nd, nd_temp;
	
	nc_c = dc*dc;
	nc_g = (dg*dg*pi)/4;
	
	bc = n/nc_c;
	nd_temp = n - bc*nc_c;
	bg = (nd_temp)/(nc_g);	
	nd = n - bc*nc_c - bg*nc_g;
	
	if((dc <= 0) || (dg <= 0))
	{
		if((dc <= 0) && (dg > 0))
		{
			nc_g = (dg*dg*pi)/4;
			bg = n/nc_g;
			nd = n - bg*nc_g;
			if(ld >= bg)
			{
				fprintf(fo, "0 %d %.3f", bg, nd);
			}
			else
			{
				bg = ld;
				nd = n - bg*nc_g;
				fprintf(fo, "0 %d %.3f", bg, nd);
			}
		}
		else if((dg <= 0) && (dc > 0))
		{
			nc_c = dc*dc;
			bc = n/nc_c;
			nd = n - bc*nc_c;
			if(ld >= bc)
			{
				fprintf(fo, "%d 0 %.3f", bc, nd);
			}
			else
			{
				bc = ld;
				nd = n - bc*nc_c;
				fprintf(fo, "%d 0 %.3f", bc, nd);
			}
		}
		else if((dc <= 0) && (dg <= 0))
		{
			fprintf(fo, "0 0 %.3f", (float)n);
		}
	}
	else
	{
		if(ld >= (bc + bg)) //ld nhieu hon so bc + bg
		{
			fprintf(fo, "%d %d %.3f", bc, bg, nd);
		}
		else if(ld < (bc + bg))
		{
			if(ld >= bc)
			{
				ld_d = ld - bc;
				bg = ld_d;
				nd = n - bc*nc_c - bg*nc_g;
				fprintf(fo, "%d %d %.3f", bc, bg, nd);	
			}
			else if(ld < bc)
			{
				bc = ld;
				nd = n - bc*nc_c;
				fprintf(fo, "%d %d %.3f", bc, bg, nd);
			}
		}
	}
}

//Rain----------------------------------------------
void rain(int n, int dc, int dg, int ld, FILE *fo)
{
	float n1 = n*1.0;
	int bc, bg, bc_m, bg_m, i;
	float nc_c, nc_g, nd, nd_m;
	
	nc_c = dc*dc;
	nc_g = (dg*dg*pi)/4;
		
	bc = n/(nc_c + nc_g);	
	bg = bc;
	nd = n - bc*nc_c - bg*nc_g;
	
	if((dc <= 0) || (dg <= 0))
	{
		if((dc <= 0) && (dg > 0))
		{
			nc_g = (dg*dg*pi)/4;
			bg = n/nc_g;
			nd = n - bg*nc_g;
			if(ld >= bg)
			{
				fprintf(fo, "0 %d %.3f", bg, nd);
			}
			else
			{
				bg = ld;
				nd = n - bg*nc_g;
				fprintf(fo, "0 %d %.3f", bg, nd);
			}
		}
		else if((dg <= 0) && (dc > 0))
		{
			nc_c = dc*dc;
			bc = n/nc_c;
			nd = n - bc*nc_c;
			if(ld >= bc)
			{
				fprintf(fo, "%d 0 %.3f", bc, nd);
			}
			else
			{
				bc = ld;
				nd = n - bc*nc_c;
				fprintf(fo, "%d 0 %.3f", bc, nd);
			}
		}
		else if((dc <= 0) && (dg <= 0))
		{
			fprintf(fo, "0 0 %.3f", (float)n);
		}
	}
	else
	{
		if(ld >= (bg + bc))	// neu ld >= bc + bg
		{
			if(dc > dg)
			{
				for(i = 1; i <= ld; i++)
				{
					if(nd >= nc_c)
					{
						bc += 1;
						nd = nd - nc_c;
					}
					if(nd >= nc_g)
					{
						bg += 1;
						nd = nd - nc_g;
					}
				}
				fprintf(fo, "%d %d %.3f", bc, bg, nd);
			}
			else if(dc < dg)
			{
				for(i = 1; i <= ld; i++)
					{
						if(nd >= nc_g)
						{
							bg += 1;
							nd = nd - nc_g;
						}
						if(nd >= nc_c)
						{
							bc += 1;
							nd = nd - nc_c;
						}
					}
					fprintf(fo, "%d %d %.3f", bc, bg, nd);
			}
		}
		else if(ld < (bc + bg))	//neu ld < bc + bg
		{
			bg = 1;
			bc = 1;
			n1 = n1 - (nc_c + nc_g);
			if(dc > dg)
			{
				for(i = 1; i <= ld; i++)
				{
					if(((bc + bg) < ld) && (n1 >= nc_c))
					{
						bc += 1;
						n1 = n1 - nc_c;
					}
					if(((bc + bg) < ld) && (n1 >= nc_g))
					{
						bg += 1;
						n1 = n1 - nc_g;
					}
				}	
				nd = n1;
				if(((bc + bg) <= ld))
				{
					fprintf(fo, "%d %d %.3f", bc, bg, nd);
				}
			}
			else if(dg > dc)
			{
				for(i = 1; i <= ld; i++)
				{
					if(((bc + bg) < ld) && (n1 >= nc_g))
					{
						bg += 1;
						n1 = n1 - nc_g;
					}
					if(((bc + bg) < ld) && (n1 >= nc_c))
					{
						bc += 1;
						n1 = n1 - nc_c;
					}
				}
				nd = n1;
				if(((bc + bg) <= ld))
				{
					fprintf(fo, "%d %d %.3f", bc, bg, nd);	
				}
			}
		}
	}
}

//Sun----------------------------------------------
void sun(int n, int dc, int dg, int ld, FILE *fo)
{
	float n1 = n*1.0;
	int bc, bg, G, H, X, i, n_m;
	float nc_c, nc_g, nd, nep;
	
	//parameter cho TH Rain
	int bc_m, bg_m;
	float nd_m;
	
	//parameter cho TH Wind
	int ld_d;
	float nd_temp;
	
	nc_c = dc*dc;
	nc_g = (dg*dg*pi)/4;
	
	if(dc < 0)
	{
		dc = 0;
	}
	
	G = dc % 6;
	H = ld % 5;
	
	if((G == 0 && H == 0) || (G == 1 && H == 1) || (G == 2 && H == 2) || (G == 3 && H == 3) || (G == 4 && H ==4))
	{
		X = 5;
	}
	else if((G == 0 && H == 1) || (G == 1 && H == 2) || (G == 2 && H == 3) || (G == 3 && H ==4) || (G == 5 && H == 0))
	{
		X = 20;
	}
	else if((G == 0 && H == 2) || ( G == 1 && H == 3) || (G == 2 && H == 4) || (G == 4 && H == 0) || (G == 5 && H == 1))
	{
		X = 15;
	}
	else if((G == 0 && H == 3) || ( G == 1 && H == 4) || (G == 3 && H == 0) || (G == 4 && H == 1) || (G == 5 && H == 2))
	{
		X = 12;
	}
	else if((G == 0 && H == 4) || (G == 2 && H == 0) || (G == 3 && H == 1) || (G == 4 && H == 2) || (G == 5 && H == 3))
	{
		X = 10;
	}
	else if((G == 1 && H == 0) || (G == 2 && H == 1) || ( G == 3 && H == 2) || (G == 4 && H == 3) || (G == 5 && H == 4))
	{
		X = 7;
	}
	
	n_m = n*(1 + 0.01*X);
	ld = ld - X;
	
	if((dc + dg) % 3 == 0)	//TH Rain----------------------------------------------
	{
		//Tinh so bc va bg theo thoi tiet Rain
		bc = n_m/(nc_c + nc_g);	
		bg = bc;
		nd = n_m - bc*nc_c - bg*nc_g;
		
		if((dc <= 0) || (dg <= 0))
		{
			if((dc <= 0) && (dg > 0))
			{
				bg = n_m/nc_g;
				nd = n_m - bg*nc_g;
				if(ld >= bg)
				{
					fprintf(fo, "0 %d %.3f", bg, nd);
				}
				else
				{
					bg = ld;
					nd = n_m - bg*nc_g;
					fprintf(fo, "0 %d %.3f", bg, nd);
				}
			}
			else if((dg <= 0) && (dc > 0))
			{
				bc = n_m/nc_c;
				nd = n_m - bc*nc_c;
				if(ld >= bc)
				{
					fprintf(fo, "%d 0 %.3f", bc, nd);
				}
				else
				{
					bc = ld;
					nd = n_m - bc*nc_c;
					fprintf(fo, "%d 0 %.3f", bc, nd);
				}
			}
			else if((dc <= 0) && (dg <= 0))
			{
				fprintf(fo, "0 0 %.3f", (float)n_m);
			}
		}
		else
		{
			if(ld > 0)
			{
				if(ld >= (bc + bg))
				{
					bc = 1;
					bg = 1;
					nd = n_m - (nc_c + nc_g);
					if(dc > dg)
					{
						for(i = 1; i <= ld; i++)
						{
							if(nd >= nc_c)
							{
								bc += 1;
								nd = nd - nc_c;
							}
							if(nd >= nc_g)
							{
								bg += 1;
								nd = nd - nc_g;
							}
						}
						fprintf(fo, "%d %d %.3f", bc, bg, nd);
					}
					else if(dc < dg)
					{
						for(i = 1; i <= ld; i++)
						{
							if(nd >= nc_g)
							{
								bg += 1;
								nd = nd - nc_g;
							}
							if(nd >= nc_c)
							{
								bc += 1;
								nd = nd - nc_c;
							}
						}
						fprintf(fo, "%d %d %.3f", bc, bg, nd);	
					}
				}
				else if(ld < (bc + bg))
				{
					bc = 1;
					bg = 1;
					n1 = n_m - (nc_c + nc_g);
					if(dc > dg)
					{
						for(i = 1; i <= ld; i++)
						{
							if(((bc + bg) < ld) && (n1 >= nc_c))
							{
								bc += 1;
								n1 = n1 - bc*nc_c;
							}
							if(((bc + bg) < ld) && (n1 >= nc_g))
							{
								bg += 1;
								n1 = n1 - bg*nc_g;
							}
						}	
						nd = n1;
						if(((bc + bg) <= ld))
						{
							fprintf(fo, "%d %d %.3f", bc, bg, nd);	
						}
					}
					else if(dg > dc)
					{
						for(i = 1; i <= ld; i++)
						{
							if(((bc + bg) < ld) && (n1 >= nc_g))
							{
								bg += 1;
								n1 = n1 - bc*nc_c;
							}
							if(((bc + bg) < ld) && (n1 >= nc_c))
							{
								bc += 1;
								n1 = n1 - bg*nc_g;
							}
						}
						nd = n1;
						if(((bc + bg) <= ld))
						{
							fprintf(fo, "%d %d %.3f", bc, bg, nd);	
						}
					}
				}
			}
			else if(ld <= 0)
			{
				fprintf(fo, "0 0 %.3f", (float)n_m);
			}
		}
	}
	else if((dc + dg) % 3 == 1)	//TH Wind----------------------------------------------
	{
		//Tinh so bc va bg theo thoi tiet Wind	
		bc = n_m/nc_c;
		nd_temp = n_m - bc*nc_c;
		bg = nd_temp/nc_g;
		nd = n_m - bc*nc_c - bg*nc_g;
		
		if((dc <= 0) || (dg <= 0))
		{
			if((dc <= 0) && (dg > 0))
			{
				bg = n_m/nc_g;
				nd = n_m - bg*nc_g;
				if(ld >= bg)
				{
					fprintf(fo, "0 %d %.3f", bg, nd);
				}
				else
				{
					bg = ld;
					nd = n_m - bg*nc_g;
					fprintf(fo, "0 %d %.3f", bg, nd);
				}
			}
			else if((dg <= 0) && (dc > 0))
			{
				bc = n_m/nc_c;
				nd = n_m - bc*nc_c;
				if(ld >= bc)
				{
					fprintf(fo, "%d 0 %.3f", bc, nd);
				}
				else
				{
					bc = ld;
					nd = n_m - bc*nc_c;
					fprintf(fo, "%d 0 %.3f", bc, nd);
				}
			}
			else if((dc <= 0) && (dg <= 0))
			{
				fprintf(fo, "0 0 %.3f", (float)n_m);
			}
		}
		else
		{
			if(ld > 0)
			{
				if(ld >= (bc + bg))
				{
					fprintf(fo, "%d %d %.3f", bc, bg, nd);
				}
				else if(ld < (bc + bg))
				{
					if(ld >= bc)
					{
						ld_d = ld - bc;
						bg = ld_d;
						nd = n_m - bc*nc_c - bg*nc_g;
						fprintf(fo, "%d %d %.3f", bc, bg, nd);	
					}
					else if(ld < bc)
					{
						bc = ld;
						nd = n_m - bc*nc_c;
						fprintf(fo, "%d 0 %.3f", bc, nd);
					}
				}
			}
			else if(ld <= 0)
			{
				fprintf(fo, "0 0 %.3f", (float)n_m);
			}
		}
	}
	else if((dc + dg) % 3 == 2)	//TH CLoud----------------------------------------------
	{
		//Tinh so bc vs bg theo thoi tiet CLoud
		bg = n_m/nc_g;
		nd_temp = n_m - bg*nc_g;
		bc = (nd_temp)/nc_c;
		nd = n_m - bg*nc_g - bc*nc_c;
		
		if(socapban(n_m, ld) == 1)
		{
			fprintf(fo, "0 0 %.3f", (float)n_m);
		}
		else if((dc <= 0) || (dg <= 0))
		{
			if((dc <= 0) && (dg > 0))
			{
				bg = n_m/nc_g;
				nd = n_m - bg*nc_g;
				if(ld >= bg)
				{
					fprintf(fo, "0 %d %.3f", bg, nd);
				}
				else
				{
					bg = ld;
					nd = n_m - bg*nc_g;
					fprintf(fo, "0 %d %.3f", bg, nd);
				}
			}
			else if((dg <= 0) && (dc > 0))
			{
				bc = n_m/nc_c;
				nd = n_m - bc*nc_c;
				if(ld >= bc)
				{
					fprintf(fo, "%d 0 %.3f", bc, nd);
				}
				else
				{
					bc = ld;
					nd = n_m - bc*nc_c;
					fprintf(fo, "%d 0 %.3f", bc, nd);
				}
			}
			else if((dc <= 0) && (dg <= 0))
			{
				fprintf(fo, "0 0 %.3f", (float)n_m);
			}
		}
		else 
		{
			if(ld > 0)
			{
				if(ld >= (bc + bg))
				{
					bg = n_m/nc_g;
					nd_temp = n_m - bg*nc_g;
					bc = nd_temp/nc_c;
					nd = n_m - bc*nc_c - bg*nc_g;
					fprintf(fo, "%d %d %.3f", bc, bg, nd);
				}
				else if(ld < (bc + bg))
				{
					if(ld >= bg)
					{
						ld_d = ld - bg;
						bc = ld_d;
						nd = n_m - bc*nc_c - bg*nc_g;
						fprintf(fo, "%d %d %.3f", bc, bg, nd);
					}
					else if(ld < bg)
					{
						bg = ld;
						nd = n_m - bg*nc_g;
						fprintf(fo, "0 %d %.3f", bg, nd);
					}
				}
			}
			else if(ld <= 0)
			{
				fprintf(fo, "0 0 %.3f", (float)n_m);
			}
		}
	}
}

//Fog----------------------------------------------
void fog(int n, int dc, int dg, FILE *fo)
{
	fprintf(fo, "%d %d %.3f", dc, dg, (float)n);
}

int socapban(int n, int ld)
{
	int sothu1=0, sothu2=0, i;
	for(i = 1; i < n; i++)
	{
		if(n % i == 0)
		{
			sothu1 += i;
		}
	}
	for(i = 1; i < ld; i++)
	{
		if(ld % i == 0)
		{
			sothu2 += i;
		}
	}
	if((n == sothu2) && (ld == sothu1))
	{
		return 1;
	}
	return 0;
}

//Cloud----------------------------------------------
void cloud(int n, int dc, int dg, int ld, FILE *fo)
{
	int bc, bg, bc_m, bg_m, i, ld_d;
	float nc_c, nc_g, nd, nd_temp;
	
	nc_c = dc*dc;
	nc_g = (dg*dg*pi)/4;
	
	bg = n/nc_g;
	nd_temp = n - bg*nc_g;
	bc = (nd_temp)/nc_c;
	nd = n - bg*nc_g - bc*nc_c;
	
	if(socapban(n, ld) == 1)
	{
		fprintf(fo, "0 0 %.3f", (float)n);
	}
	else if((dc <= 0) || (dg <= 0))
	{
		if((dc <= 0) && (dg > 0))
		{
			nc_g = (dg*dg*pi)/4;
			bg = n/nc_g;
			nd = n - bg*nc_g;
			if(ld >= bg)
			{
				fprintf(fo, "0 %d %.3f", bg, nd);
			}
			else
			{
				bg = ld;
				nd = n - bg*nc_g;
				fprintf(fo, "0 %d %.3f", bg, nd);
			}
		}
		else if((dg <= 0) && (dc > 0))
		{
			nc_c = dc*dc;
			bc = n/nc_c;
			nd = n - bc*nc_c;
			if(ld >= bc)
			{
				fprintf(fo, "%d 0 %.3f", bc, nd);
			}
			else
			{
				bc = ld;
				nd = n - bc*nc_c;
				fprintf(fo, "%d 0 %.3f", bc, nd);
			}
		}
		else if((dc <= 0) && (dg <= 0))
		{
			fprintf(fo, "0 0 %.3f", (float)n);
		}
	}
	else 
	{
		if(ld >= (bc + bg))
		{
			fprintf(fo, "%d %d %.3f", bc, bg, nd);
		}
		else if(ld < (bc + bg))
		{
			if(ld >= bg)
			{
				ld_d = ld - bg;
				bc = ld_d;
				nd = n - bc*nc_c - bg*nc_g;
				fprintf(fo, "%d %d %.3f", bc, bg, nd);
			}
			else if(ld < bg)
			{
				bg = ld;
				nd = n - bg*nc_g;
				fprintf(fo, "0 %d %.3f", bg, nd);
			}
		}
	}
}
